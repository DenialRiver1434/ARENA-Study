# Code from Pytorch docs
# I will commentate

# USING OFFICIAL PYTORCH DATASETS

import torch
from torchvision import datasets
from torchvision.transforms import v2

Fashion_training_data = datasets.FashionMNIST(
    root="data", # Location
    train=True, # Specifies this is for training
    download=True, # Download from internet since not local
    transform=v2.Compose([ # composes the following two transformations
        v2.ToImage(), # converts to image type
        v2.ToDtype(torch.float32, scale=True) # sets everything to 32-bit float
    ])
)

Fashion_test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)])
)

import os
import pandas as pd
from torchvision.io import decode_image
from torch.utils.data import Dataset

# CUSTOM DATASETS

class CustomImageDataset(Dataset): 
    # ^ Auto-inherits all Dataset functions ^
    # "Dataset" inheritance also requires implementing the following

    # Call using dataset = CustomImageDataset("labels.csv", "images/")
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        # =========
        #        IMPORTANT:
        # THIS PART CAN BE ANYTHING
        # =========
        # Here is an example with images

        # annotations_file currently a CSV
        # CSV read using pd.read_csv
        self.img_labels = pd.read_csv(annotations_file)

        # file path for images
        self.img_dir = img_dir

        # SEE TRANSFORMS.PY
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        # Also can return anything; this is only an example
        # for image recognition

        # join can only join same type due to settings.json
        # so added a str()
        img_path = os.path.join(self.img_dir, str(self.img_labels.iloc[idx, 0]))
        image = decode_image(img_path)
        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label
