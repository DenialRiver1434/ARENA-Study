import torch

x = torch.ones(5)  # input tensor
y = torch.zeros(3)  # expected output

 # TURN ON REQUIRES_GRAD TO COMPUTE GRAD DESCENT
w = torch.randn(5, 3, requires_grad=True)
b = torch.randn(3, requires_grad=True)
z = torch.matmul(x, w)+b
loss = torch.nn.functional.binary_cross_entropy_with_logits(z, y)

loss.backward()
print(w.grad)
print(b.grad)