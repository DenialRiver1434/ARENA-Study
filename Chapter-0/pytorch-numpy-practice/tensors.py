# BRIEF Tensors testing

import torch 
import numpy as np

v = torch.tensor((np.arange(4) + 1).reshape(2, 2))

x_ones = torch.ones_like(v) # retains the properties of x_data
print(f"Ones Tensor: \n {x_ones} \n")

# Concat
print(torch.cat([torch.arange(5), torch.rand(4)]))

# Matrix mult
m = torch.rand((2, 2))
print(m + 5)
print(m @ m.T)