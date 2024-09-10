RSNA_Anomaly_Detection
===

Motivation and Introduction
---

Since chest X-rays (CXRs) are widely used in the diagnosis of thoracic diseases, and existing supervised learning models for diagnostic assistance have issues with high costs and the difficulty of collecting rare disease data, we aim to explore unsupervised learning methods to assist in diagnosis.This time, we used three unsupervised learning models to detect abnormalities in chest X-rays

Methodology
---

We used Reconstruction-Based Models, which learn the appearance of normal images and generate images that resemble normal ones for any input. Since we assume the generated images are normal, if there is a significant difference between the original image and the generated one, the original image is likely to be abnormal. Here are the three models we used: [BiGAN](BiGAN "游標顯示"), [VAE-GAN](VAEGAN "游標顯示"), and [AnoDDPM](AnoDDPM "游標顯示"). You can find more detailed descriptions in their respective folders.
