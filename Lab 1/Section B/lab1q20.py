import numpy as np 

np.random.seed(42)

matrix = np.random.randint(1, 50, 16).reshape(4, 4)
determinant = np.linalg.det(matrix)
print(f"Transpose: \n{matrix.T} \nDeterminant: \n{determinant:.4f}")

if abs(determinant) > 1e-10:
    print(f"Inverse: \n{np.linalg.inv(matrix)}")
else:
    print("Matrix is singular, no inverse exists")