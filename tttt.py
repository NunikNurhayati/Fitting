from matplotlib import pyplot as plt
import numpy as np

sample = np.random.normal(size=10)
sample = [0,0,4,4,2,3,2,2,1,1,1,0,4,4]
print sample

vert_hist = np.histogram(sample, bins=3)
print vert_hist
ax1 = plt.subplot(2, 1, 1)
ax1.plot(vert_hist[0], vert_hist[1][:-1], '*g')

ax2 = plt.subplot(2, 1, 2)
ax2.hist(sample, bins=5, orientation="horizontal");
plt.show()