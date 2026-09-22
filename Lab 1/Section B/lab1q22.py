import numpy as np

np.random.seed(42)

nums = [int(x) for x in input("Enter 10 Numbers: ").split()]

arr = np.array(nums)
print(f"Array: {arr} \nSorted: {np.sort(arr)} \nMedian: {np.median(arr)}")