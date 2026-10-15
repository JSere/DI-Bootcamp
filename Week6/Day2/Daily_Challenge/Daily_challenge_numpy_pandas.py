import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set a random seed for reproducibility
np.random.seed(42)

# 1. Data Preparation
# Generate synthetic monthly temperatures for 10 cities over 12 months (-5 to 35 degrees Celsius)
temperatures = np.random.uniform(low=-5.0, high=35.0, size=(10, 12))

# Define city names and month labels
cities = [
    "City A",
    "City B",
    "City C",
    "City D",
    "City E",
    "City F",
    "City G",
    "City H",
    "City I",
    "City J",
]
months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]

# Create a Pandas DataFrame
df_temps = pd.DataFrame(temperatures, index=cities, columns=months)
print("Temperature DataFrame:")
print(df_temps.round(2))
print("-" * 50)

# 2. Data Analysis
# Calculate the annual average temperature for each city (mean across columns / axis=1)
annual_avg = df_temps.mean(axis=1)
print("Annual Average Temperature per City:")
print(annual_avg.round(2))
print("-" * 50)

# Identify the city with the highest and lowest average temperature
highest_city = annual_avg.idxmax()
lowest_city = annual_avg.idxmin()

print(f"City with the highest average annual temperature: {highest_city} ({annual_avg[highest_city]:.2f}°C)")
print(f"City with the lowest average annual temperature: {lowest_city} ({annual_avg[lowest_city]:.2f}°C)")
print("-" * 50)

# 3. Data Visualization
plt.figure(figsize=(12, 6))

# Plot temperature trends for each city
for city in df_temps.index:
    plt.plot(df_temps.columns, df_temps.loc[city], marker="o", label=city, alpha=0.7)

plt.title("Monthly Temperature Trends Across Different Cities", fontsize=14, fontweight="bold")
plt.xlabel("Months", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

# Show the plot
plt.show()