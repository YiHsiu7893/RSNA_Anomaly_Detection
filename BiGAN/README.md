# BiGAN

## Reference
* paper: [Efficient GAN-Based Anomaly Detection](https://arxiv.org/abs/1802.06222 "游標顯示")
* github: [Efficient-GAN-Anomaly-Detection](https://github.com/houssamzenati/Efficient-GAN-Anomaly-Detection/tree/master "游標顯示")

## Architechture
<img src="https://github.com/YiHsiu7893/RSNA_Anomaly_Detection/blob/main/BiGAN/pic/BiGAN.jpg" width=60% height=60%>

## Installation
Run:  
```
pip install -r requirements.txt
```

## Preparation
Put **training_data.csv**, **testing_data.csv** and **valid_data.csv** into `data/`.  
  
Run:  
```
python data/makedata.py
```

## Training
Run:  
```
python main.py bigan mnist run --nb_epochs=<number_epochs> --label=1 --w=<float between 0 and 1> --d=<int>
```
  
To reproduce the results of the paper, please use w=0.1 (as in the original AnoGAN paper which gives a weight of 0.1 to the discriminator loss), d=1 for the feature matching loss.  
  
Images of ROC curve and distribution histograms will be saved at `results/bigan/mnist/fm/{w}`.

## Image Reconstruction
Put your images in `data/visCXR/ori`.  
  
Run:  
```
python main.py bigan mnist run --nb_epochs=0 --label=1
```
  
Reconstructed images will be saved at `data/visCXR/rec`.

## Heatmap Generation
Run:  
```
python plot_heatmap.py
```
  
Heatmap will be saved at `data/visCXR/heatmap`.
