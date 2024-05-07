import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc, average_precision_score, precision_recall_curve, auc


def do_prc(scores, true_labels, file_name='', directory='', plot=True):
    """ Does the PRC curve

    Args :
            scores (list): list of scores from the decision function
            true_labels (list): list of labels associated to the scores
            file_name (str): name of the PRC curve
            directory (str): directory to save the jpg file
            plot (bool): plots the PRC curve or not
    Returns:
            prc_auc (float): area under the under the PRC curve
    """
    precision, recall, thresholds = precision_recall_curve(true_labels, scores)
    prc_auc = auc(recall, precision)

    if plot:
        plt.figure()
        plt.step(recall, precision, color='b', alpha=0.2, where='post')
        plt.fill_between(recall, precision, step='post', alpha=0.2, color='b')
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.ylim([0.0, 1.05])
        plt.xlim([0.0, 1.0])
        plt.title('Precision-Recall curve: AUC=%0.4f' 
                            %(prc_auc))
        if not os.path.exists(directory):
            os.makedirs(directory)
        plt.savefig('results/' + file_name + '_prc.jpg')
        plt.close()

    return prc_auc


def do_roc(scores, true_labels, file_name='', directory='', plot=True):
    """Does the ROC curve.

    Args:
        scores (list): List of scores from the decision function.
        true_labels (list): List of true labels associated with the scores.
        file_name (str): Name of the ROC curve file.
        directory (str): Directory to save the JPG file.
        plot (bool): Whether to plot the ROC curve or not.

    Returns:
        roc_auc (float): Area under the ROC curve (AUROC).
    """
    fpr, tpr, thresholds = roc_curve(true_labels, scores)
    #np.savez('BiGAN_roc_data_others.npz', fpr=fpr, tpr=tpr, thresholds=thresholds)

    roc_auc = auc(fpr, tpr)

    if plot:
        plt.figure()
        plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.4f)' % roc_auc)
        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver Operating Characteristic (ROC) Curve')
        plt.legend(loc='lower right')
        if not os.path.exists(directory):
            os.makedirs(directory)
        plt.savefig('results/' + file_name + '_roc.jpg')
        plt.close()

    return roc_auc

def score_distribution(scores, true_labels, file_name='', directory='', plot=True):
    scores_label0 = [score for score, label in zip(scores, true_labels) if label == 0]
    scores_label1 = [score for score, label in zip(scores, true_labels) if label == 1]

    # 绘制标签0和1的分数分布
    plt.figure(figsize=(10, 6))
    plt.hist(scores_label0, bins=50, color='blue', alpha=0.5, label='Label 0')
    plt.hist(scores_label1, bins=50, color='red', alpha=0.5, label='Label 1')
    plt.xlabel('Scores')
    plt.ylabel('Frequency')
    plt.title('Scores Distribution for Label 0 and 1')
    plt.legend()
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.savefig('results/' + file_name + '_distribution.jpg')
    #plt.show()