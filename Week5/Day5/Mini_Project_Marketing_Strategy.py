import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else '.'
file_path = os.path.join(script_dir, 'US Superstore data.xls')

df = pd.read_excel(file_path, sheet_name='Orders')

top_states = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(5)
ny_ca = df[df['State'].isin(['New York', 'California'])].groupby('State')[['Sales', 'Profit']].sum()
ny_cust = df[df['State'] == 'New York'].groupby(['Customer ID', 'Customer Name'])[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False).head(1)

cp = df.groupby('Customer ID')['Profit'].sum().sort_values(ascending=False)
t20_profit_ratio = cp.head(int(len(cp) * 0.20)).sum() / cp.sum() * 100

city_agg = df.groupby('City')[['Sales', 'Profit']].sum()
top_cities_sales = city_agg.sort_values(by='Sales', ascending=False).head(20)
top_cities_profit = city_agg.sort_values(by='Profit', ascending=False).head(20)

cust_sales_series = df.groupby('Customer ID')['Sales'].sum().sort_values(ascending=False)
t20_sales_ratio = cust_sales_series.head(int(len(cust_sales_series) * 0.20)).sum() / cust_sales_series.sum() * 100

print(top_states)
print(ny_ca)
print(ny_cust)
print(f"Top 20% Profit Ratio: {t20_profit_ratio:.2f}%")
print(f"Top 20% Sales Ratio: {t20_sales_ratio:.2f}%")
