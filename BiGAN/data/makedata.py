import os
import pandas as pd
import pydicom
from PIL import Image
import numpy as np

# 讀取 training_data.csv 文件
train_data = pd.read_csv('training_data.csv')
valid_data = pd.read_csv('valid_data.csv')
test_data = pd.read_csv('testing.csv')

# 提取 full_path 欄位的照片名稱
train_images = (train_data['full_path'].apply(lambda x: x.split('\\')[-1]), train_data['label'])
valid_images = (valid_data['full_path'].apply(lambda x: x.split('\\')[-1]), valid_data['label'])
test_images = (test_data['full_path'].apply(lambda x: x.split('\\')[-1]), test_data['label'])

# 定義原始圖片文件夾
source_folder = 'stage_2_train_images'

data = {}
data["x_test"] = []
data["x_train"] = []
data["x_valid"] = []
data["y_test"] = []
data["y_train"] = []
data["y_valid"] = []
train = valid = test = 0
for filename in os.listdir(source_folder):
    source_path = os.path.join(source_folder, filename)
    dcm = pydicom.dcmread(source_path)
    image = Image.fromarray(dcm.pixel_array).resize((64, 64))
    image_array = (np.array(image)/ 255.0).flatten()

    if filename in train_images[0].tolist():
        data["x_train"].append(image_array)
        data["y_train"].append(train_images[1].tolist()[train_images[0].tolist().index(filename)])  # 將對應的標籤存入 y_train
        train += 1
    if filename in valid_images[0].tolist():
        data["x_valid"].append(image_array)
        data["y_valid"].append(valid_images[1].tolist()[valid_images[0].tolist().index(filename)])  # 將對應的標籤存入 y_valid
        valid += 1
    if filename in test_images[0].tolist():
        data["x_test"].append(image_array)
        data["y_test"].append(test_images[1].tolist()[test_images[0].tolist().index(filename)])  # 將對應的標籤存入 y_test
        test += 1

print(train, "images are for training.")
print(valid, "images are for validation.")
print(test, "images are for testing.")

np.savez("size64.npz", **data)
