import numpy as np
import pandas as pd

df = pd.read_csv("vgsales.csv")

# Exercise 1
bins = np.arange(0, df["EU_Sales"].max() + 5, 5)
df["EU_Sales_bins"] = pd.cut(df["EU_Sales"], bins=bins, right=False)
eu_sales_binned = (
    df.dropna(subset=["EU_Sales"])
    .groupby("EU_Sales_bins")
    .size()
    .reset_index(name="Count")
)

# Exercise 2
df["Profitability_Index"] = (
    df["Global_Sales"] - (df["Global_Sales"] * 0.30)
) / df["Global_Sales"]
top_profitable = df.sort_values(by="Profitability_Index", ascending=False)

# Exercise 3
df["Sales_Performance_Index"] = df["Global_Sales"].rank(
    ascending=False, method="min"
)

# Exercise 4
yearly_sales = (
    df.groupby("Year")["Global_Sales"].sum().reset_index().sort_values("Year")
)
yearly_sales["YoY_Growth_Rate"] = yearly_sales["Global_Sales"].pct_change()

# Exercise 5
genre_sales = df.groupby("Genre")["Global_Sales"].sum().reset_index()
total_global_sales = df["Global_Sales"].sum()
genre_sales["Genre_Dominance_Ratio"] = (
    genre_sales["Global_Sales"] / total_global_sales
)

# Exercise 6
df["NA_Sales_Share"] = df["NA_Sales"] / df["Global_Sales"]
custom_result = df.groupby("Genre")["NA_Sales_Share"].mean().reset_index()