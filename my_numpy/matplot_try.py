

import matplotlib.pyplot as plt
import numpy as np


stichprobe = np.random.randint(0, 256, size=10000)
# plt.hist(stichprobe, bins=256)
ssize = 10
data = [stichprobe[ssize*i:ssize*(i+1)].mean() for i in range(len(stichprobe)/ssize)]
print(len(data))
plt.hist(data, bins=100)
plt.title("Weird Plot")
plt.xlabel("X Label")
plt.ylabel("Y Label")

plt.xlim(0, 256)
plt.show()