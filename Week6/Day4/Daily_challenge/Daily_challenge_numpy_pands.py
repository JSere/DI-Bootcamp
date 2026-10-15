import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Exercise 1
np.random.seed(42)
matrix_1 = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]], dtype=float)
det_1 = np.linalg.det(matrix_1)
inv_1 = np.linalg.inv(matrix_1)
print(f"Determinant: {det_1:.2f}")
print("Inverse:")
print(inv_1)

# Exercise 2
np.random.seed(42)
arr_2 = np.random.rand(50)
mean_2 = np.mean(arr_2)
median_2 = np.median(arr_2)
std_2 = np.std(arr_2)
print(f"Mean: {mean_2:.2f}, Median: {median_2:.2f}")
print(f"Standard Deviation: {std_2:.2f}")

# Exercise 3
dates_3 = np.arange(
    np.datetime64("2023-01-01"), np.datetime64("2023-02-01"), dtype="datetime64[D]"
)
formatted_dates_3 = np.datetime_as_string(dates_3, unit="D")
formatted_dates_3 = [d.replace("-", "/") for d in formatted_dates_3]
print(formatted_dates_3)

# Exercise 4
np.random.seed(42)
df_4 = pd.DataFrame(
    np.random.rand(5, 4), columns=["Col1", "Col2", "Col3", "Col4"]
)
filtered_4 = df_4[df_4["Col1"] > 0.5]
sum_4 = df_4.sum()
avg_4 = df_4.mean()
print("Filtered DataFrame (Col1 > 0.5):")
print(filtered_4)
print("Sum:")
print(sum_4)
print("Average:")
print(avg_4)

# Exercise 5
# Grayscale images are represented as 2D arrays where each value represents a pixel intensity (e.g., 0 to 255).
image_5 = np.random.randint(0, 256, size=(5, 5), dtype=np.uint8)
print("5x5 Grayscale Image Array:")
print(image_5)

# Exercise 6
np.random.seed(42)
productivity_before = np.random.normal(loc=50, scale=10, size=30)
productivity_after = productivity_before + np.random.normal(
    loc=5, scale=3, size=30
)
mean_diff = np.mean(productivity_after - productivity_before)
print(f"Null Hypothesis: The training program has no effect (mean difference <= 0).")
print(f"Alternative Hypothesis: The training program increases productivity (mean difference > 0).")
print(f"Mean Productivity Difference: {mean_diff:.2f}")

# Exercise 7
np.random.seed(42)
array_a = np.random.rand(5)
array_b = np.random.rand(5)
comparison_7 = array_a > array_b
print(f"Array A: {array_a}")
print(f"Array B: {array_b}")
print(f"Comparison (A > B): {comparison_7}")

# Exercise 8
time_series_8 = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
ts_series = pd.Series(np.random.rand(len(time_series_8)), index=time_series_8)
jan_mar = ts_series["2023-01-01":"2023-03-31"]
apr_jun = ts_series["2023-04-01":"2023-06-30"]
jul_sep = ts_series["2023-07-01":"2023-09-30"]
oct_dec = ts_series["2023-10-01":"2023-12-31"]
print(f"Jan-Mar length: {len(jan_mar)}")
print(f"Apr-Jun length: {len(apr_jun)}")
print(f"Jul-Sep length: {len(jul_sep)}")
print(f"Oct-Dec length: {len(oct_dec)}")

# Exercise 9
np_arr_9 = np.array([[1, 2], [3, 4]])
df_from_np_9 = pd.DataFrame(np_arr_9, columns=["A", "B"])
np_from_df_9 = df_from_np_9.to_numpy()
print("DataFrame from NumPy:")
print(df_from_np_9)
print("NumPy array from DataFrame:")
print(np_from_df_9)

# Exercise 10
np.random.seed(42)
x_10 = np.arange(10)
y_10 = np.random.rand(10)
plt.figure(figsize=(6, 4))
plt.plot(x_10, y_10, marker="o")
plt.title("Line Graph of Random Numbers")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()