# Sales data
sales_data = [
    {"Product_Name": "Laptop", "Quantity_Sold": 15},
    {"Product_Name": "Mouse", "Quantity_Sold": 20},
    {"Product_Name": "Laptop", "Quantity_Sold": 10},
    {"Product_Name": "Keyboard", "Quantity_Sold": 12},
    {"Product_Name": "Mouse", "Quantity_Sold": 18},
    {"Product_Name": "Monitor", "Quantity_Sold": 8},
    {"Product_Name": "Laptop", "Quantity_Sold": 5},
    {"Product_Name": "Printer", "Quantity_Sold": 7},
    {"Product_Name": "Keyboard", "Quantity_Sold": 10}
]

# Calculate total quantity sold for each product
product_sales = {}

for item in sales_data:
    product = item["Product_Name"]
    qty = item["Quantity_Sold"]

    if product in product_sales:
        product_sales[product] += qty
    else:
        product_sales[product] = qty

# Sort products by quantity sold (highest first)
top_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)

print("Top 5 Products Sold the Most:\n")

for product, qty in top_products[:5]:
    print(product, ":", qty)
