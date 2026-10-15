import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'train.csv')

# Load the Titanic dataset using the absolute path
df = pd.read_csv(file_path)

# --- Exercise 1: Duplicate Detection and Removal ---
duplicates_before = df.duplicated().sum()
df = df.drop_duplicates()
print(f"# Exercise 1: Duplicates before: {duplicates_before}, after: {df.duplicated().sum()}")

# --- Exercise 2: Handling Missing Values ---
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Cabin'] = df['Cabin'].fillna('Unknown')
print("# Exercise 2: Missing values handled (Age, Embarked, Cabin)")

# --- Exercise 3: Feature Engineering ---
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
rare_titles = ['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona']
df['Title'] = df['Title'].replace(rare_titles, 'Rare')
df['Title'] = df['Title'].replace(['Mlle', 'Ms'], 'Miss')
df['Title'] = df['Title'].replace('Mme', 'Mrs')
print("# Exercise 3: Features engineered (FamilySize, Title)")

# --- Exercise 4: Outlier Detection and Handling ---
fare_cap = df['Fare'].quantile(0.98)
df['Fare'] = np.where(df['Fare'] > fare_cap, fare_cap, df['Fare'])
print("# Exercise 4: Outliers handled for Fare via quantile capping")

# --- Exercise 5: Data Standardization and Normalization ---
scaler = StandardScaler()
df['Age_Standardized'] = scaler.fit_transform(df[['Age']])
df['Fare_Standardized'] = scaler.fit_transform(df[['Fare']])
print("# Exercise 5: Numerical features standardized (Age, Fare)")

# --- Exercise 6: Feature Encoding ---
df = pd.get_dummies(df, columns=['Sex', 'Embarked', 'Title'], drop_first=True, dtype=int)
print("# Exercise 6: Categorical variables one-hot encoded")

# --- Exercise 7: Data Transformation for Age Feature ---
bins = [0, 12, 18, 60, 100]
labels = ['Child', 'Teen', 'Adult', 'Senior']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
df = pd.get_dummies(df, columns=['AgeGroup'], drop_first=False, dtype=int)
print(f"# Exercise 7: Age binned and encoded. Final dataset shape: {df.shape}")