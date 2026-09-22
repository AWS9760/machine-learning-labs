import numpy as np

np.random.seed(42)

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
dotProduct = 0

for i in range(len(a)):
    dotProduct += a[i] * b[i]

print(f"Dot product: {dotProduct} \nVerification by np.dot: {np.dot(a, b)}")