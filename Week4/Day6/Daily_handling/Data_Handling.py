import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.decomposition import PCA

# Load the Data Science Job Salary dataset using absolute path
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'datascience_salaries.csv')
df = pd.read_csv(file_path)

# --- Task 1: Normalize the 'salary' column using Min-Max normalization ---
scaler = MinMaxScaler()
df['salary_normalized'] = scaler.fit_transform(df[['salary']])
print("--- Normalized Salary (Min: 0, Max: 1) ---")
print(df[['salary', 'salary_normalized']].head())

# --- Task 2: Implement Dimensionality Reduction (PCA) ---
# Select numerical columns for PCA processing
num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
X = df[num_cols].dropna()

# Standardize numerical features before applying PCA
scaler_pca = StandardScaler()
X_scaled = scaler_pca.fit_transform(X)

# Reduce dimensions to 2 principal components
pca = PCA(n_components=2)
principal_components = pca.fit_transform(X_scaled)
print(f"\n--- PCA Dimensionality Reduction ---")
print(f"Original shape: {X_scaled.shape} -> Reduced shape: {principal_components.shape}")
print(f"Explained Variance Ratio: {pca.explained_variance_ratio_}")

# --- Task 3: Group by 'experience_level' and calculate average and median salary ---
salary_aggregation = df.groupby('experience_level')['salary'].agg(['mean', 'median', 'count']).reset_index()
salary_aggregation.rename(columns={'mean': 'average_salary', 'median': 'median_salary'}, inplace=True)

print(f"\n--- Salary Aggregation by Experience Level ---")
print(salary_aggregation)