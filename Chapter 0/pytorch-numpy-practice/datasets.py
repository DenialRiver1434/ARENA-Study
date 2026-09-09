import torch
from torchvision import datasets
from torchvision.transforms import v2
import matplotlib.pyplot as plt

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
