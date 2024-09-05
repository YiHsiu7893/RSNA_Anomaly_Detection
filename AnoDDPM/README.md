AnoDDPM
===
 ### 原始的paper
> #### [AnoDDPM: Anomaly Detection with Denoising Diffusion Probabilistic Models using Simplex Noise](https://ieeexplore.ieee.org/document/9857019 "游標顯示")
 ### 我們用的code  
> #### [AnoDDPM](https://github.com/Julian-Wyatt/AnoDDPM "游標顯示")

### Diffusion Model的架構圖
><img src="https://github.com/YiHsiu7893/RSNA_Anomaly_Detection/blob/main/AnoDDPM/pictures/diffusion_model_flow_chart.png" width=60% height=60%>

### 各檔案描述
> [makenpy.py](makenpy.py "游標顯示")
>> 資料處理，從csv檔中讀取圖片的路徑並讀取圖片，並將所有圖片轉為後續訓練、測試使用的.npy檔，因我們的原始圖片是dicom檔，若有要讀取其他格式的圖片要修改程式碼。

> [dataset.py](dataset.py "游標顯示")
>>設定及讀取datasets，在351行的init_datasets中可更改要使用的datasets。

> [detection.py](dataset.py "游標顯示")
>> 

> [diffusion_training.py](diffusion_training.py "游標顯示")
>> 

> [evaluation.py](evaluation.py "游標顯示")
>> 

> [GaussianDiffusion.py](GaussianDiffusion.py "游標顯示")
>> 

> [graphs.py](graphs.py "游標顯示")
>> 

> [simplex.py](simplex.py "游標顯示")
>>

> [UNet.py](UNet.py "游標顯示")
>> 

> [helpers.py](helpers.py "游標顯示")
>>

### 使用方法
> training
>>使用 python diffusion_training.py [args number]，例如：
> 
> ```python
> python diffusion_training.py 28
> ```
> 
> ```python
> python testing.py
> ```
> 
>  ```python
> python heatmap.py
> ```
>  (原始的code是說用python3，但我們用python3跑不了反而是python跑得了)
> 

