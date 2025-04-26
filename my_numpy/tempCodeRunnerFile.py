import matplotlib.pyplot as plt
import numpy as np

stichprobe = np.random.random(2000)
plt.hist(stichprobe, bins=100)
plt.title("Weird Plot")
plt.xlabel("X Label")
plt.ylabel("Y Label")
#plt.ylim(0, 100)
#plt.xlim(0, 100)
plt.show()