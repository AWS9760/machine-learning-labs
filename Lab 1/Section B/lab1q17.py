import numpy as np

np.random.seed(42)

arr = np.array([10,20,30,40,50])
normalized = (arr - arr.min()) / (arr.max() - arr.min())
print(f"Normalized: {normalized}")