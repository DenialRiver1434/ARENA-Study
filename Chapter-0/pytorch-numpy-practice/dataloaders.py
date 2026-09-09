
import torch
from torchvision import datasets
from torchvision.transforms import v2

training_data = datasets.FashionMNIST(root="data",train=True,download=True,transform=v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)]))
test_data = datasets.FashionMNIST(root="data",train=False,download=True,transform=v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)]))

# Dataloader helps batch data so it can be iterated

from torch.utils.data import DataLoader

train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=64, shuffle=True)

# Get a batch
train_features, train_labels = next(iter(train_dataloader))

print(f"Labels batch shape: {train_labels.size()}") # 64 labels