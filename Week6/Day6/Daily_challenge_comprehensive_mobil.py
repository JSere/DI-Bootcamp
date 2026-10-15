import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import seaborn as sns

# Load dataset (assuming 'train.csv' is in your working directory)
df = pd.read_csv("train.csv")

# Initial structure check
print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())

# Feature data types and non-null counts
print("\nDataset Info:")
print(df.info())

# Summary statistics for overview
print("\nDescriptive Statistics:")
print(df.describe())