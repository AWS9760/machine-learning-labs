import numpy as np

np.random.seed(42)

arr = np.random.randint(1, 101, 25)
print(f"Sum: {arr.sum()} \nMean: {arr.mean():.2f} \nStandard Deviation: {arr.std():.2f}")