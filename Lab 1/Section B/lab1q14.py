import numpy as np

np.random.seed(42)

arr = np.arange(1, 17).reshape(4, 4)
diag = np.diag(arr)
print(f"Diagonal: {diag} \nSum: {diag.sum()}")