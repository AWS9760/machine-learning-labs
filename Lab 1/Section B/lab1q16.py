import numpy as np

np.random.seed(42)

temps = np.random.randint(30, 48, 30)
hot_days = temps[temps > 38]
print(f"Hot Day: {hot_days} \nTotal: {hot_days.size}")