AnoDDPM
===
 ### 原始的paper
> #### [AnoDDPM: Anomaly Detection with Denoising Diffusion Probabilistic Models using Simplex Noise](https://ieeexplore.ieee.org/document/9857019 "游標顯示")
 ### 我們用的code  
> #### [AnoDDPM](https://github.com/Julian-Wyatt/AnoDDPM "游標顯示")

### Diffusion Model的架構圖
><img src="https://github.com/YiHsiu7893/RSNA_Anomaly_Detection/blob/main/AnoDDPM/pictures/diffusion_model_flow_chart.png" width=60% height=60%>

### 各檔案描述
> [test_args](test_args "游標顯示")
>> training及testing過程中使用的所有變數，包含epoch數、使用的添加noise方式、圖片大小等。

>> 
> [makenpy.py](makenpy.py "游標顯示")
>> 我們自己新增的檔案，用來做資料處理，從csv檔中讀取圖片的路徑並讀取圖片，並將所有圖片轉為後續訓練、測試使用的.npy檔，因我們的原始圖片是dicom檔，若有要讀取其他格式的圖片要修改程式碼。

> [dataset.py](dataset.py "游標顯示")
>>設定及讀取datasets，在351行的init_datasets中可更改要使用的datasets，相較於原版的loader使用cycle並限制每個epoch train的data數量，我們有新增了一個testing_dataset_loadery在375行，使testing時會保證test完所有testing dataset中的所有data。

> [diffusion_training.py](diffusion_training.py "游標顯示")
>> training的過程。

> [evaluation.py](evaluation.py "游標顯示")
>> testing的過程，改為計算error score與繪製ROC curve為主。

> [GaussianDiffusion.py](GaussianDiffusion.py "游標顯示")
>> Diffusion Model的架構。

> [simplex.py](simplex.py "游標顯示")
>>使用simplex作為加入noise的方法時使用的相關定義與functions。

> [UNet.py](UNet.py "游標顯示")
>> UNet Model。

> [helpers.py](helpers.py "游標顯示")
>>作者自定義的functions，26行的load_checkpoint與51行的load_parameters中能調整要使用哪份權重。

### 使用方法
> training
>>使用 python diffusion_training.py [args number]，例如：
>> 
>> ```python
>> python diffusion_training.py 28
>> ```
> testing
>>使用 python evaluation.py [args number]，例如：
>> ```python
>> python evaluation.py 28
>> ```
>  (原始的code是說用python3，但我們用python3跑不了反而是python跑得了)
> 

