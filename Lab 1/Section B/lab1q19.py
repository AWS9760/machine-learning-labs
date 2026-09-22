import numpy as np

np.random.seed(42)

arr = np.arange(1, 11)
result = np.where(arr % 2 == 0, -1, arr)
print(f"Result: {result}")