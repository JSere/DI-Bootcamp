import numpy as np

# Exercise 1
arr1 = np.arange(10)
print(arr1)

# Exercise 2
arr2 = np.array([3.14, 2.17, 0, 1, 2], dtype=int)
print(arr2)

# Exercise 3
arr3 = np.arange(1, 10).reshape(3, 3)
print(arr3)

# Exercise 4
np.random.seed(42)  # Optional: for reproducible random numbers
arr4 = np.random.rand(4, 5)
print(arr4)

# Exercise 5
given_array_5 = np.array([[21, 22, 23, 22, 22], [20, 21, 22, 23, 24], [21, 22, 23, 22, 22]])
arr5 = given_array_5[1]
print(arr5)

# Exercise 6
given_array_6 = np.arange(10)
arr6 = given_array_6[::-1]
print(arr6)

# Exercise 7
arr7 = np.eye(4)
print(arr7)

# Exercise 8
given_array_8 = np.arange(10)
total_sum = np.sum(given_array_8)
average = np.mean(given_array_8)
print(f"Sum: {total_sum}, Average: {average}")

# Exercise 9
arr9 = np.arange(1, 21).reshape(4, 5)
print(arr9)

# Exercise 10
given_array_10 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr10 = given_array_10[given_array_10 % 2 != 0]
print(arr10)