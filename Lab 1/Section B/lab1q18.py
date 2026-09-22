import numpy as np

np.random.seed(42)

marks = np.random.randint(50, 100, (5, 3))
totals = marks.sum(axis=1)
averages = marks.mean(axis=1)
print(f"Marks: {marks} \nTotals: {totals} \nAverages: {averages}")