import numpy as np

np.random.seed(42)

matrix = np.eye(6)
np.fill_diagonal(matrix, [1,2,3,4,5,6])
print(f"Array:\n{matrix}")