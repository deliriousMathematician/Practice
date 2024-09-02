import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np

fig, axs = plt.subplots(1,2, figsize=(6,6))
axs[0].plot([1,2,3,4],[2,1,4,3])
axs[1].plot([3,4,5,6],[1,2,3,4])
axs[0].set_title('test')
plt.show()