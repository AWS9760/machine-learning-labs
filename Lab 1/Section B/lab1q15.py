import numpy as np

np.random.seed(42)

a = np.random.randint(1, 5, (3, 3))
b = np.random.randint(1, 5, (3, 3))

print(f"Element-wise Multiplication: \n{a * b} \n\nMatrix Multiplication: \n{a @ b}")
