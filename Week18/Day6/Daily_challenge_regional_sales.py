import pandas as pd

df = pd.read_csv("vgsales.csv")

df["EU_Sales_Pct"] = df["EU_Sales"] / df["Global_Sales"]
df["NA_Sales_Pct"] = df["NA_Sales"] / df["Global_Sales"]
df["JP_Sales_Pct"] = df["JP_Sales"] / df["Global_Sales"]
df["Other_Sales_Pct"] = df["Other_Sales"] / df["Global_Sales"]

regional_yearly_sales = (
    df.groupby("Year")[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]]
    .sum()
    .reset_index()
    .sort_values("Year")
)