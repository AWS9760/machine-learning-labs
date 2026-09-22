import numpy as np

np.random.seed(42)

def is_symmetric(arr):
    return np.array_equal(arr, arr.T)

symmetric = np.array([[1,2,3], [2,4,5], [3,5,6]])
notSymmetric = np.array([[1,2], [3,4]])
print(f"Is 1st Array symmetric: {is_symmetric(symmetric)} \nIs 2nd Array symmetric: {is_symmetric(notSymmetric)}")