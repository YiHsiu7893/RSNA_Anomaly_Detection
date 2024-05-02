import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import torchvision.utils as vutils
import pandas as pd
import pydicom
from torch.utils.data import DataLoader, Dataset
from PIL import Image
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


# load dicom
"""class CustomDataset(Dataset):
    def __init__(self, dataframe, transform=None):
        self.dataframe = dataframe
        self.transform = transform

    def __len__(self):
        return len(self.dataframe)

    def __getitem__(self, idx):
        img_path = self.dataframe.iloc[idx, 0]
        dcm_data = pydicom.dcmread(img_path)

        image = dcm_data.pixel_array
        image = Image.fromarray(image)
        label = int(self.dataframe.iloc[idx, 1])

        if self.transform:
            image = self.transform(image)

        return image, label"""

#load png or jpg    
class CustomDataset(Dataset):
    def __init__(self, dataframe, transform=None):
        self.dataframe = dataframe
        self.transform = transform

    def __len__(self):
        return len(self.dataframe)

    def __getitem__(self, idx):
        img_path = self.dataframe.iloc[idx, 0]
        image = Image.open(img_path).convert('L') 

        label = int(self.dataframe.iloc[idx, 1])

        if self.transform:
            image = self.transform(image)

        return image, label

def dataloader(batch_size):
  data_entry = pd.read_csv('testing.csv')
  print(data_entry)
  data_entry.columns = ['full_path', 'Label']
  transform=transforms.Compose([ transforms.Resize(64),transforms.CenterCrop(64),transforms.ToTensor(),transforms.Normalize((0.5),(0.5))])
  dataset=CustomDataset(data_entry, transform=transform)
  data_loader = DataLoader(dataset, batch_size=64, shuffle=True)
  return data_loader
