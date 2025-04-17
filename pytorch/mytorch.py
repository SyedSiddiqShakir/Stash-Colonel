import torch
import matplotlib.pyplot as plt

x = torch.linspace(0, 2 * torch.pi, steps=100)

y = torch.sin(x)

x_np = x.numpy()
y_np = y.numpy()

plt.figure()
plt.plot(x_np, y_np)             
plt.title("Sine Wave via PyTorch")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()
