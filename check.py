import torch

# Assuming MPS is available
device = torch.device("mps")
model = model.to(device)