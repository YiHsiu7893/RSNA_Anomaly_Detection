import torch
from torch.autograd import Variable
torch.autograd.set_detect_anomaly(True)
from dataloader import dataloader
from models import VAE_GAN, Encoder
import os
from tqdm import tqdm 
import csv
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
import pandas as pd

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

data_loader=dataloader(64)
gen=VAE_GAN().to(device)
Enc=Encoder().to(device)

weights_path =  'model_weight/generator/generator_weights_50.pth' 
if os.path.exists(weights_path):
    gen.load_state_dict(torch.load(weights_path))
    print("use pretrained weight") 

thresholds = [i for i in range(360, 440, 40)]
best_threshold = 0
best_f1 = 0

true_labels = []
code_norm = []


# Predict and collect true labels and reconstruction errors
for data, label in tqdm(data_loader, desc="testing"):
    
    datav = Variable(data).to(device)
    mean, logvar, rec_enc = gen(datav)
    reconstruct_error = torch.abs(rec_enc - datav)
    reconstruct_error = reconstruct_error.view(reconstruct_error.size(0), -1).sum(dim=1)
    
    #sampling epsilon from normal distribution
    true_labels.extend(label.cpu().numpy())
    code_norm.extend(reconstruct_error.detach().cpu().numpy())

# Convert lists to numpy arrays
fpr, tpr, thresholds = metrics.roc_curve(true_labels, code_norm)

# Calculate AUC
auc = metrics.auc(fpr, tpr)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='red', lw=2, label='ROC curve (area = %0.2f)' % auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()
