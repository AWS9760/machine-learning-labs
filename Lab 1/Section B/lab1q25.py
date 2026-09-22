import numpy as np

np.random.seed(42)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.array([[9, 10], [11, 12]])
v = np.vstack([a, b, c])
h = np.hstack([a, b, c])

print(f"vstack shape: {v.shape} (rows grow)\n{v}")
print(f"hstack shape: {h.shape} (rows grow)\n{h}")