RSNA_Anomaly_Detection
===

Motivation and Introduction
---
Since chest X-rays (CXRs) are widely used in the diagnosis of thoracic diseases, and existing supervised learning models for diagnostic assistance have issues with high costs and the difficulty of collecting rare disease data, we aim to explore unsupervised learning methods to assist in diagnosis.
This time, we used three unsupervised learning models to detect abnormalities in chest X-rays  
    
    

Methodology
---

  We used Reconstruction-Based Models, which learn the appearance of normal images and generate images that resemble normal ones for any input. Since we assume the generated images are normal, if there is a significant difference between the original image and the generated one, the original image is likely to be abnormal.  
  Here are the three models we used: [BiGAN](BiGAN "游標顯示"), [VAE-GAN](VAE-GAN "游標顯示"), and [AnoDDPM](AnoDDPM "游標顯示"). You can find more detailed descriptions in their respective folders.  
  

Dataset
---
  Our dataset is sourced from the [RSNA](https://www.kaggle.com/c/rsna-pneumonia-detection-challenge/data "游標顯示") and is primarily used for detecting pneumonia. The original dataset contains three categories: 'Normal,' 'Opacity,' and 'Not Normal.' For the purpose of our study, we combined the 'Opacity' and 'Not Normal' categories into a single category labeled 'Abnormal,' while retaining the 'Normal' category as is.  
  All chest images are resized to 64x64 pixels, and only 70% of the 'Normal' cases are used for training the model.  
  

Result
---
  We used the L1 norm between the reconstructed image and the original image as the error score and plotted the ROC curve based on it.Below are the ROC curves for the four methods.We found VAE-GAN (represented in red) and DDPM with Simplex noise (represented in green) perform the best, with an AUROC of 0.77.
  ><img src="https://github.com/YiHsiu7893/RSNA_Anomaly_Detection/blob/main/pictures/ROC_curve.png" width=100% height=100%>  
  In addition, we also evaluated the models' ability to identify abnormal regions. We performed pixel-wise subtraction between the reconstructed image and the original image and highlighted the differences in red. The redder the area, the greater the difference. Below are three examples: the first image is a normal image, while the other two are CXRs with abnormalities.
  Normal case
  ><img src="https://github.com/YiHsiu7893/RSNA_Anomaly_Detection/blob/main/pictures/compare_normal.png" width=100% height=100%> 
  
  Abnormal case
  ><img src="https://github.com/YiHsiu7893/RSNA_Anomaly_Detection/blob/main/pictures/compare_abnormal1.png" width=100% height=100%> 
  ><img src="https://github.com/YiHsiu7893/RSNA_Anomaly_Detection/blob/main/pictures/compare_abnormal2.png" width=100% height=100%> 
  

