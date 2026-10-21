import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r'c:\Users\Juan Serebrinsky\Documents\DI-Bootcamp\Week5\Daily_challenge\US Superstore data.xls', sheet_name='Orders')

df['Year'] = df['Order Date'].dt.year
yearly_sales = df.groupby('Year')['Sales'].sum()

plt.figure(figsize=(10, 5))
plt.plot(yearly_sales.index, yearly_sales.values, marker='o', color='#1f77b4', linewidth=2.5, markersize=8)
plt.title('Annual Sales Trends (2014 - 2017)', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(yearly_sales.index)
plt.tight_layout()
plt.show()

state_sales = df.groupby('State')['Sales'].sum().nlargest(10)

plt.figure(figsize=(12, 6))
state_sales.plot(kind='bar', color='#2ca02c', edgecolor='black')
plt.title('Top 10 States by Total Sales', fontsize=14, fontweight='bold')
plt.xlabel('State', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

top_products = df.groupby('Product Name')['Sales'].sum().nlargest(10).reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(data=top_products, x='Sales', y='Product Name', palette='Blues_r')
plt.title('Top 10 Products by Total Sales', fontsize=14, fontweight='bold')
plt.xlabel('Total Sales ($)', fontsize=12)
plt.ylabel('Product Name', fontsize=12)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Discount', y='Profit', alpha=0.5, hue='Category', palette='Set1')
plt.title('Profit vs. Discount by Category', fontsize=14, fontweight='bold')
plt.xlabel('Discount Rate', fontsize=12)
plt.ylabel('Profit ($)', fontsize=12)
plt.axhline(0, color='red', linestyle='--', linewidth=1, label='Break-even (Zero Profit)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()