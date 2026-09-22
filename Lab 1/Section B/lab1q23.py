import numpy as np

np.random.seed(42)

arr = np.arange(1, 13).reshape(3, 4)
selected = arr[np.ix_([0, 2], [1, 3])]
print(f"Array: \n{arr} \nSelected: \n{selected}")