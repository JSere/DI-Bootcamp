import os
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for plots
sns.set_theme(style="whitegrid")

# Locate and load the dataset dynamically using absolute path
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'Airplane_Crashes_and_Fatalities_Since_1908_t0_2023.csv')

# Load dataset with latin1 encoding to handle special historical characters
df = pd.read_csv(file_path, encoding='latin1')


df['Parsed_Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Year'] = df['Parsed_Date'].dt.year.fillna(df['Date'].astype(str).str.extract(r'(\d{4})')[0].astype(float))
df['Decade'] = (df['Year'] // 10) * 10

# Calculate survival rates
df['Survival_Rate'] = 1 - (df['Fatalities'] / df['Aboard'])
df.loc[df['Aboard'] == 0, 'Survival_Rate'] = np.nan


total_crashes = len(df)
mean_fatalities = df['Fatalities'].mean()
median_fatalities = df['Fatalities'].median()
std_fatalities = df['Fatalities'].std()

print("=== EXPLORATORY DATA ANALYSIS ===")
print(f"Total Crashes: {total_crashes}")
print(f"Mean Fatalities per Crash: {mean_fatalities:.2f}")
print(f"Median Fatalities per Crash: {median_fatalities:.2f}")
print(f"Standard Deviation of Fatalities: {std_fatalities:.2f}")


fatalities_1970s = df[df['Decade'] == 1970]['Fatalities'].dropna()
fatalities_2000s = df[df['Decade'] == 2000]['Fatalities'].dropna()

t_stat, p_val = stats.ttest_ind(fatalities_1970s, fatalities_2000s, equal_var=False)
print("\n=== STATISTICAL ANALYSIS (T-Test) ===")
print(f"T-statistic (1970s vs 2000s fatalities): {t_stat:.4f}")
print(f"P-value: {p_val:.4e}")


# Chart 1: Crashes Over Time
plt.figure(figsize=(10, 5))
yearly_crashes = df['Year'].value_counts().sort_index()
sns.lineplot(x=yearly_crashes.index, y=yearly_crashes.values, color='firebrick', linewidth=2)
plt.title('Number of Airplane Crashes Per Year (1908 - 2023)', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Crashes', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'crashes_per_year.png'), dpi=300)
plt.close()

# Chart 2: Fatalities Distribution Histogram
plt.figure(figsize=(10, 5))
sns.histplot(df['Fatalities'].dropna(), bins=50, kde=True, color='darkblue')
plt.title('Distribution of Fatalities per Crash', fontsize=14, fontweight='bold')
plt.xlabel('Number of Fatalities', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.xlim(0, 200)
plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'fatalities_distribution.png'), dpi=300)
plt.close()

print("\nAnalysis completed successfully. Visualizations generated and saved.")