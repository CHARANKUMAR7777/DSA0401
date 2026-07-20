# Property Data
property_data = [
    {"Property_ID": 101, "Location": "Chennai", "Bedrooms": 3, "Area": 1500, "Listing_Price": 4500000},
    {"Property_ID": 102, "Location": "Coimbatore", "Bedrooms": 5, "Area": 2200, "Listing_Price": 6500000},
    {"Property_ID": 103, "Location": "Chennai", "Bedrooms": 4, "Area": 1800, "Listing_Price": 5000000},
    {"Property_ID": 104, "Location": "Madurai", "Bedrooms": 6, "Area": 3000, "Listing_Price": 8500000},
    {"Property_ID": 105, "Location": "Coimbatore", "Bedrooms": 5, "Area": 2500, "Listing_Price": 7000000}
]

# 1. Average listing price in each location
location_price = {}
location_count = {}

for property in property_data:
    location = property["Location"]
    price = property["Listing_Price"]

    if location in location_price:
        location_price[location] += price
        location_count[location] += 1
    else:
        location_price[location] = price
        location_count[location] = 1

print("1. Average Listing Price in Each Location")
for location in location_price:
    average = location_price[location] / location_count[location]
    print(location, ":", average)

# 2. Number of properties with more than four bedrooms
count = 0
for property in property_data:
    if property["Bedrooms"] > 4:
        count += 1

print("\n2. Number of Properties with More Than 4 Bedrooms:", count)

# 3. Property with the largest area
largest = property_data[0]

for property in property_data:
    if property["Area"] > largest["Area"]:
        largest = property

print("\n3. Property with the Largest Area")
print("Property ID:", largest["Property_ID"])
print("Location:", largest["Location"])
print("Bedrooms:", largest["Bedrooms"])
print("Area:", largest["Area"])
print("Listing Price:", largest["Listing_Price"])
