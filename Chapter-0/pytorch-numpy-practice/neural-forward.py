import torch
from torch import nn

class NeuralNetwork(nn.Module):
    # nn.Module has __call__ function
    # INPUT: n x 28 x 28

    def __init__(self):
        super().__init__()

        # self.flatten is a function calling nn.Flatten()
        # Makes the n x 28 x 28 tensor into nx  784-length
        self.flatten = nn.Flatten()

        # self.linear_relu_stack is also a function
        self.linear_relu_stack = nn.Sequential(
            # n x 784 -> n x 512 matrix
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
            # Outputs n x 10 matrix
        )

    def forward(self, x):
        # One forward pass

        x = self.flatten(x)
        # Goes through the neural network
        logits = self.linear_relu_stack(x)
        return logits

# Uses GPU/Cuda/... acceleration
device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu"
# Loads the model with the accelerator
model = NeuralNetwork().to(device)

# Gives the model a 28x28 starting matrix
X = torch.rand(3, 28, 28, device=device)

# Sends X to the model and it goes through a forward pass
# nn.Module has __call__ function which we inherit
logits = model(X)

# Run a softmax on the output to make it probabilities
pred_probab = nn.Softmax(dim=1)(logits)

# y_pred is the prediction with highest probability
y_pred = pred_probab.argmax(1)
print(f"Predicted class: {y_pred}")