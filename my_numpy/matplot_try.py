

import matplotlib.pyplot as plt
import numpy as np

"""
stichprobe = np.random.randint(0, 256, size=10000)
plt.hist(stichprobe, bins=256)
plt.title("Weird Plot")
plt.xlabel("X Label")
plt.ylabel("Y Label")
#plt.ylim(0, 100)
#plt.xlim(0, 100)
plt.show()
"""

# Bell curve


stichprobe = np.random.randn(10000)

count, bins, _ = plt.hist(
    stichprobe,
    bins=50,
    density=True,
    alpha=0.6,
    color="steelblue",
    label="Data"
)

x = np.linspace(bins[0], bins[-1], 200)
pdf = (1 / np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2)

plt.plot(x, pdf, "r", linewidth=2, label="Curve Line")
plt.title("Bell Curve")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()

plt.show()

