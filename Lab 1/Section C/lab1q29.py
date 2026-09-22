import matplotlib
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(500)
plt.figure(figsize=(7, 4))
plt.hist(data, bins=20, color="mediumpurple", edgecolor="black")
plt.axvline(data.mean(), color="red", linestyle="--", label=f"mean={data.mean():.2f}")
plt.title("Histogram of 500 Normal Random Numbers")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.savefig("q29_histogram.png", dpi=150)
plt.show()
plt.close()