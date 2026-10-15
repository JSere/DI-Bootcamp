import numpy as np

# Exercise 1
np.random.seed(42)
arr1 = np.random.rand(5, 5)
arr1[arr1 == arr1.max()] = 0
print(arr1)

# Exercise 2
np.random.seed(42)
array1 = np.random.rand(5)
array2 = np.random.rand(5)
arr2 = np.intersect1d(array1, array2)
print(arr2)

# Exercise 3
np.random.seed(42)
arr3 = np.random.rand(10)
ascending = np.sort(arr3)
descending = np.sort(arr3)[::-1]
print(f"Ascending: {ascending}")
print(f"Descending: {descending}")

# Exercise 4
np.random.seed(42)
arr4 = np.random.rand(4, 4)
rank = np.linalg.matrix_rank(arr4)
print(f"Rank: {rank}")

# Exercise 5
arr5 = np.ones((5, 5), dtype=int)
arr5[1:-1, 1:-1] = 0
print(arr5)