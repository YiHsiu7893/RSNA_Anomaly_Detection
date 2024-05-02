#繪製reconstruct的圖片

import torch
from torch.autograd import Variable
torch.autograd.set_detect_anomaly(True)
from dataloader import dataloader
from models import VAE_GAN
import os
from tqdm import tqdm 
import matplotlib.pyplot as plt

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

data_loader=dataloader(64)
gen1=VAE_GAN().to(device)
gen50=VAE_GAN().to(device)
    
weights_path =  'model_weight/generator/generator_weights_50.pth' 
if os.path.exists(weights_path):
    gen50.load_state_dict(torch.load(weights_path))
    print("use pretrained weight") 

count = 0

save_dir = "image_results"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
    
for data, label in tqdm(data_loader, desc='Testing'):
    data = data.to(device)
    print(data.shape)
    
    mean, logvar, rec_enc = gen50(data)
    

    for i in range(len(data)):
        data_np = data[i].squeeze().cpu().numpy()
        rec_enc_np50 = rec_enc[i].squeeze().cpu().detach().numpy()

        original_image_path = os.path.join(save_dir, "original_image_{}.png".format(count))
        plt.imsave(original_image_path, data_np, cmap='gray')

        reconstructed_image_path50 = os.path.join(save_dir, "reconstructed_{}.png".format(count))
        plt.imsave(reconstructed_image_path50, rec_enc_np50, cmap='gray')


        count += 1



# heatmap

import cv2
import matplotlib.pyplot as plt
import numpy as np

for i in range(64):
    ori_path = "image_results/original_image_{}.png".format(i)
    ori = cv2.imread(ori_path)
    ori = cv2.resize(ori, (64, 64))
    ori = ori.astype(np.float32)

    rec_path = "image_results/reconstructed_{}.png".format(i)
    rec = cv2.imread(rec_path)
    rec = rec.astype(np.float32)


    # 計算絕對差值並平方
    mask = np.square(np.abs(ori - rec))

    mask = mask / 255

    heatmap = cv2.applyColorMap(np.uint8(mask), cv2.COLORMAP_HOT)
    cam = heatmap + ori
    cam = (cam/np.max(cam))*255

    cv2.imwrite("image_results/heatmap_{}.jpg".format(i), cam)