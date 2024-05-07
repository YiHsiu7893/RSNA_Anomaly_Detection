# BiGAN

## Reference
* paper: [Efficient GAN-Based Anomaly Detection](https://arxiv.org/abs/1802.06222 "游標顯示")
* github: [Efficient-GAN-Anomaly-Detection](https://github.com/houssamzenati/Efficient-GAN-Anomaly-Detection/tree/master "游標顯示")

## Architechture

## Installation
    pip install -r requirements.txt


## Preparation
Put **training_data.csv**, **testing_data.csv** and **valid_data.csv** into `data/`  
and run `python data/makedata.py`

## Training
    python main.py bigan mnist run --nb_epochs=<number_epochs> --label=1 --w=<float between 0 and 1> --m='fm' --d=<int> --rd=<int>  
To reproduce the results of the paper, please use w=0.1 (as in the original AnoGAN paper which gives a weight of 0.1 to the discriminator loss), d=1 for the feature matching loss.  
The result will in `results/bigan/mnist/fm/{w}`
