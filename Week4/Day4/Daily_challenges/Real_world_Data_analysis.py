"""
Case Study: Daily E-Commerce Sales Analysis

1. Business Context:
   An online store records its daily transactions. The data team needs to process 
   this information quickly to calculate total revenue and identify the best-selling 
   product of the day to make inventory decisions.

2. Data Analysis Methodology & Role:
   Using Python data structures (lists of dictionaries) and aggregation logic, 
   raw transaction records are filtered, multiplied (price x quantity), and grouped 
   to extract actionable business insights instantly.

3. Significance & Impact:
   Without data analysis, tracking inventory and revenue manually would be slow 
   and prone to human error. Automating this analysis allows businesses to react 
   rapidly to consumer demand and optimize stock management.
"""

# --- Python Implementation ---

sales_data = [
    {"product": "Laptop", "price": 1200, "quantity": 2},
    {"product": "Mouse", "price": 25, "quantity": 10},
    {"product": "Keyboard", "price": 75, "quantity": 5},
    {"product": "Monitor", "price": 300, "quantity": 3},
    {"product": "Mouse", "price": 25, "quantity": 4}
]

# Calculate total revenue
total_revenue = sum(item["price"] * item["quantity"] for item in sales_data)

# Aggregate quantities per product
product_sales = {}
for item in sales_data:
    prod = item["product"]
    qty = item["quantity"]
    product_sales[prod] = product_sales.get(prod, 0) + qty

# Find the top-selling product
top_product = max(product_sales, key=product_sales.get)

# Output results
print(f"Total Revenue: ${total_revenue}")
print(f"Top-Selling Product: {top_product} ({product_sales[top_product]} units)")