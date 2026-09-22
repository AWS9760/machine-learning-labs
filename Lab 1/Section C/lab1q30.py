import matplotlib
import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1, 11)
y = np.random.randint(10, 100, 10)
fig, ax = plt.subplots(2, 2, figsize=(10, 8))
ax[0, 0].plot(x, y, color="tab:blue")
ax[0, 0].set_title("Line")
ax[0, 1].bar(x, y, color="tab:green")
ax[0, 1].set_title("Bar")
ax[1, 0].scatter(x, y, color="tab:red")
ax[1, 0].set_title("Scatter")
ax[1, 1].hist(y, bins=5, color="tab:orange", edgecolor="black")
ax[1, 1].set_title("Histogram")
fig.suptitle("Same Dataset, Four Chart Types")
plt.tight_layout()
plt.savefig("q30_subplots_grid.png", dpi=150)
plt.show()
plt.close()