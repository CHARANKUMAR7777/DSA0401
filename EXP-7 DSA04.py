#e commerce
import pandas as pd

# Load dataset
order_data = pd.read_csv("order_data.csv")

# Convert Order_Date to datetime
order_data["Order_Date"] = pd.to_datetime(order_data["Order_Date"])

# 1. Total number of orders made by each customer
print("1. Total Orders by Each Customer")
print(order_data.groupby("Customer_ID").size())

# 2. Average order quantity for each product
print("\n2. Average Order Quantity for Each Product")
print(order_data.groupby("Product_Name")["Order_Quantity"].mean())

# 3. Earliest and Latest Order Dates
print("\n3. Earliest Order Date")
print(order_data["Order_Date"].min())

print("\nLatest Order Date")
print(order_data["Order_Date"].max())
nn
