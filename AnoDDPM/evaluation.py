import matplotlib.pyplot as plt
import matplotlib.animation as animation

import torch
from skimage.metrics import structural_similarity as ssim
from sklearn.metrics import auc, roc_curve

from helpers import gridify_output
from tqdm import tqdm
import numpy as np
import cv2

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def main():
    pass


def precision(real_mask, recon_mask):
    TP = ((real_mask == 1) & (recon_mask == 1))
    FP = ((real_mask == 1) & (recon_mask == 0))
    return torch.sum(TP).float() / ((torch.sum(TP) + torch.sum(FP)).float() + 1e-6)



def recall(real_mask, recon_mask):
    TP = ((real_mask == 1) & (recon_mask == 1))
    FN = ((real_mask == 0) & (recon_mask == 1))
    return torch.sum(TP).float() / ((torch.sum(TP) + torch.sum(FN)).float() + 1e-6)


def FPR(real_mask, recon_mask):
    FP = ((real_mask == 1) & (recon_mask == 0))
    TN = ((real_mask == 0) & (recon_mask == 0))
    return torch.sum(FP).float() / ((torch.sum(FP) + torch.sum(TN)).float() + 1e-6)


def ROC_AUC(real_mask, square_error):
    if type(real_mask) == torch.Tensor:
        return roc_curve(real_mask.detach().cpu().numpy().flatten(), square_error.detach().cpu().numpy().flatten())
    else:
        return roc_curve(real_mask.flatten(), square_error.flatten())


def AUC_score(fpr, tpr):
    return auc(fpr, tpr)


def testing(testing_dataset_loader, diffusion, args, ema, model):
    print("start testing")
    """
    Samples videos on test set & calculates some metrics such as PSNR & VLB.
    PSNR for diffusion is found by sampling x_0 to T//2 and then finding a prediction of x_0

    :param testing_dataset_loader: The cycle(dataloader) object for looping through test set
    :param diffusion: Gaussian Diffusion model instance
    :param args: parameters of the model
    :param ema: exponential moving average unet for sampling
    :param model: original unet for VLB calc
    :return: outputs:
                total VLB    mu +- sigma,
                prior VLB    mu +- sigma,
                vb -> T      mu +- sigma,
                x_0 mse -> T mu +- sigma,
                mse -> T     mu +- sigma,
                PSNR         mu +- sigma
    """
    import os
    try:
        os.makedirs(f'./diffusion-videos/ARGS={args["arg_num"]}/test-set/')
    except OSError:
        pass
    ema.eval()
    model.eval()
    print("set to evaluation mode")

   
    error_scores = []
    for data in tqdm(testing_dataset_loader, desc="Processing Test Data", total = len(testing_dataset_loader)):
        #data = next(testing_dataset_loader)
        if args["dataset"] != "cifar":
            x = data["image"]
            x = x.to(device)
        else:
            # cifar outputs [data,class]
            x = data[0].to(device)
        
        #print(args["T"])
        out = diffusion.forward_backward(ema, x, see_whole_sequence=None, denoise_fn = "noise_fn", t_distance=200) #args["T"] // 2
    
        """
        x_img = x.squeeze().cpu().detach().numpy()
        out_img = out.squeeze().cpu().detach().numpy()
        
        x_img_path = 'diffusion-training-images/x_img_abnormal2_e2000_t200.png'
        out_img_path = 'diffusion-training-images/out_img_abnormal2_e2000_t200.png'
        plt.imsave(x_img_path, x_img, cmap='gray')
        plt.imsave(out_img_path, out_img, cmap='gray')
        
        fig, axes = plt.subplots(1, 2, figsize=(10, 5))

        axes[0].imshow(x_img, cmap='gray')
        axes[0].set_title('Original Image (x)')
        axes[0].axis('off')

        axes[1].imshow(out_img, cmap='gray')
        axes[1].set_title('Processed Image (out)')
        axes[1].axis('off')

        plt.tight_layout()

        plt.show()
        """
        
        x_np = x.cpu().detach().numpy()
        out_np = out.cpu().detach().numpy()

        error_map = np.abs(x_np - out_np)

        error_score = np.sum(error_map)

        error_scores.append(error_score) 
    return error_scores


def main():
    args, output = load_parameters(device)
    print(f"args{args['arg_num']}")

    in_channels = 3 if args["dataset"].lower() == "cifar" else 1
    unet = UNetModel(
            args['img_size'][0], args['base_channels'], channel_mults=args['channel_mults'], in_channels=in_channels
            )
    ema = UNetModel(
            args['img_size'][0], args['base_channels'], channel_mults=args['channel_mults'], in_channels=in_channels
            )

    betas = get_beta_schedule(args['T'], args['beta_schedule'])

    diff = GaussianDiffusionModel(
            args['img_size'], betas, loss_weight=args['loss_weight'],
            loss_type=args['loss-type'], noise=args["noise_fn"]
            )

    ema.load_state_dict(output["ema"])
    ema.to(device)
    ema.eval()

    unet.load_state_dict(output["model_state_dict"])
    unet.to(device)
    unet.eval()
    _, testing_dataset_normal, testing_dataset_abnormal = dataset.init_datasets("./", args)
    
    num_testing_normal_samples = len(testing_dataset_normal)
    num_testing_abnormal_samples = len(testing_dataset_abnormal)

    print(f"Number of samples in testing normal dataset: {num_testing_normal_samples}")
    print(f"Number of samples in testing abnormal dataset: {num_testing_abnormal_samples}")
    
    testing_dataset_loader_normal = dataset.testing_dataset_loader(testing_dataset_normal, args)
    testing_dataset_loader_abnormal = dataset.testing_dataset_loader(testing_dataset_abnormal, args)

    print("testing normal data")
    error_scores_normal = testing(testing_dataset_loader_normal, diff, args, ema, unet)
    print("testing abnormal data")
    error_scores_abnormal = testing(testing_dataset_loader_abnormal, diff, args, ema, unet)
    
    error_scores = error_scores_normal + error_scores_abnormal
    labels = [0] * len(error_scores_normal) + [1] * len(error_scores_abnormal)

    fpr, tpr, thresholds = roc_curve(labels, error_scores)
    np.savez('AnoDDPM_roc_data_e2000_t80.npz', fpr=fpr, tpr=tpr, thresholds=thresholds)
    roc_auc = auc(fpr, tpr)
    
    plt.figure()
    lw = 2
    plt.plot(fpr, tpr, color='darkorange',
            lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC)')
    plt.legend(loc="lower right")
    plt.show()



if __name__ == '__main__':
    import dataset
    import os
    import matplotlib.animation as animation
    import numpy as np
    from GaussianDiffusion import GaussianDiffusionModel, get_beta_schedule
    from UNet import UNetModel
    from detection import load_parameters

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    main()
