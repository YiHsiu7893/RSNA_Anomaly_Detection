AnoDDPM
===
 ### Original Paper
> #### [AnoDDPM: Anomaly Detection with Denoising Diffusion Probabilistic Models using Simplex Noise](https://ieeexplore.ieee.org/document/9857019 "游標顯示")
 ### Code We Used  
> #### [AnoDDPM](https://github.com/Julian-Wyatt/AnoDDPM "游標顯示")

### Architecture Diagram of the Diffusion Model
><img src="https://github.com/YiHsiu7893/RSNA_Anomaly_Detection/blob/main/AnoDDPM/pictures/diffusion_model_flow_chart.png" width=60% height=60%>

### File Descriptions
> [test_args](test_args "游標顯示")
>> All variables used during the training and testing process, including the number of epochs, the method of adding noise, image size, etc.

>> 
> [makenpy.py](makenpy.py "游標顯示")
>> A custom file we added for data processing. It reads image paths from a CSV file, reads the images, and converts them into .npy files for subsequent training and testing. Since our original images are in DICOM format, the code needs to be modified if you want to read other formats.

> [dataset.py](dataset.py "游標顯示")
>>Sets up and reads the datasets. You can change the datasets used in the init_datasets at line 351. Compared to the original loader, which uses a cycle and limits the amount of data trained per epoch, we added a testing_dataset_loader at line 375 to ensure that all data in the testing dataset is tested.

> [diffusion_training.py](diffusion_training.py "游標顯示")
>> The training process.

> [evaluation.py](evaluation.py "游標顯示")
>> The testing process, modified mainly to calculate the error score and plot the ROC curve. You can use the code in the commented-out section at line 91 to obtain the reconstructed images and heatmaps.

> [GaussianDiffusion.py](GaussianDiffusion.py "游標顯示")
>> The architecture of the Diffusion Model.

> [simplex.py](simplex.py "游標顯示")
>> Definitions and functions related to using simplex noise as the method for adding noise.
> [UNet.py](UNet.py "游標顯示")
>> The UNet Model.

> [helpers.py](helpers.py "游標顯示")
>> Custom functions defined by the author. In the load_checkpoint at line 26 and load_parameters at line 51, you can adjust which weights to use.

### Usage Instructions
> training
>>Use python diffusion_training.py [args number], for example:
>> 
>> ```python
>> python diffusion_training.py 28
>> ```
> testing
>>Use python evaluation.py [args number], for example:
>> ```python
>> python evaluation.py 28
>> ```
>  (The original code suggests using python3, but we found that it only works with python, not python3.)
> 

AnoDDPM(中文版)
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
>> testing的過程，改為計算error score與繪製ROC curve為主，使用91行被註解掉的部分的code可以獲得reconstructed image與heatmap。

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

