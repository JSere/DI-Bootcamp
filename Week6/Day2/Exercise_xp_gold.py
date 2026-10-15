import numpy as np

# Exercise 1
np.random.seed(42)
arr1 = np.random.rand(5, 5)
print(f"Min: {arr1.min():.2f}, Max: {arr1.max():.2f}")

# Exercise 2
np.random.seed(42)
arr2 = np.random.rand(3, 3)
normalized_arr2 = (arr2 - arr2.mean()) / arr2.std()
print(normalized_arr2)

# Exercise 3
arr3 = np.linspace(0, 10, 50, endpoint=False)
print(arr3)

# Exercise 4
np.random.seed(42)
matrix_a = np.random.rand(5, 3)
matrix_b = np.random.rand(3, 2)
arr4 = matrix_a @ matrix_b
print(arr4)

# Exercise 5
matrix_x = np.array([[1, 2, 3], [4, 5, 6]])
matrix_y = np.array([[7, 8], [9, 1], [2, 3]])
arr5 = matrix_x @ matrix_y
print(arr5)