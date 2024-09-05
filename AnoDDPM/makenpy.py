import pandas as pd
import pydicom
import numpy as np
import os


csv_file = "training_data.csv"
data = pd.read_csv(csv_file)

output_folder = "./"

os.makedirs(output_folder, exist_ok=True)

all_images = []

for index, row in data.iterrows():
    dicom_file_path = row['full_path']
    dcm_data = pydicom.dcmread(dicom_file_path)
    image_array = dcm_data.pixel_array
    all_images.append(image_array)

all_images_array = np.stack(all_images)

npy_file_path = os.path.join(output_folder, "Train.npy")
np.save(npy_file_path, all_images_array)

print(f"已將所有圖片儲存為 {npy_file_path}")


"""import pandas as pd
import pydicom
import numpy as np
import os

# 讀取 CSV 文件
csv_file = "testing_data_1000.csv"
data = pd.read_csv(csv_file)
#random_data = data.sample(n=1000, random_state=42)
#random_data.to_csv("testing_data_1000.csv", index=False)
#print(random_data.shape)

# 儲存 .npy 檔案的目錄
output_folder_normal = "C:\CSproject\AnoDDPM\DATASETS\Test_normal"
output_folder_abnormal = "C:\CSproject\AnoDDPM\DATASETS\Test_opacity"



# 遍歷 CSV 文件中的每一行
for index, row in data.iterrows():

    dicom_file_path = row['full_path']
    
    dcm_data = pydicom.dcmread(dicom_file_path)

    image_array = dcm_data.pixel_array
    
    label = row['label']
    if label == 1:
        output_folder = output_folder_abnormal
    else:
        output_folder = output_folder_normal
    
    npy_file_path = os.path.join(output_folder, f"image_{index}.npy")
    np.save(npy_file_path, image_array)
    """
    
"""import cv2
import numpy as np

img_path = r'C:\CSproject\VAE_GAN\VAE-GAN-PYTORCH-master\VAE-GAN-PYTORCH-master\image_results\new_CXRs\ori_3.png'
img = cv2.imread(img_path)

if img is None:
    print("Error: Unable to read the image.")
else:
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print("Image shape:", gray_img.shape)
    
    img_array = np.array(gray_img)
    
    npy_path = r'C:\CSproject\AnoDDPM\DATASETS\Test_label_abnormal2\org.npy'
    np.save(npy_path, img_array)
    
    print(f"Numpy array saved to {npy_path}")"""
