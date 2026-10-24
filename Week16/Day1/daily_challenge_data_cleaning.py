import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# 1. Load Dataset
# Replace 'globalterrorismdb.csv' with your actual file path
df = pd.read_csv('globalterrorismdb.csv', encoding='latin1', low_memory=False)

# 2. Data Cleaning
selected_cols = ['iyear', 'imonth', 'iday', 'country_txt', 'region_txt', 'attacktype1_txt', 'nkill', 'nwound']
df_clean = df[selected_cols].copy()

df_clean['nkill'] = df_clean['nkill'].fillna(0)
df_clean['nwound'] = df_clean['nwound'].fillna(0)
df_clean = df_clean.dropna(subset=['country_txt', 'region_txt', 'attacktype1_txt'])
df_clean['iyear'] = df_clean['iyear'].astype(int)

# 3. Data Transformation
df_transformed = pd.get_dummies(df_clean, columns=['attacktype1_txt'], drop_first=True)

scaler = StandardScaler()
df_transformed[['nkill_scaled', 'nwound_scaled']] = scaler.fit_transform(df_transformed[['nkill', 'nwound']])

# 4. Exploratory Data Analysis & Visualization
plt.figure(figsize=(12, 6))
sns.countplot(data=df_transformed, x='region_txt', order=df_transformed['region_txt'].value_counts().index)
plt.xticks(rotation=45, ha='right')
plt.title('Terrorism Events by Region')
plt.xlabel('Region')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
yearly_trend = df_transformed.groupby('iyear').size().reset_index(name='event_count')
sns.lineplot(data=yearly_trend, x='iyear', y='event_count')
plt.title('Global Terrorism Events Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Events')
plt.tight_layout()
plt.show()