import pandas as pd
from sklearn.tree import DecisionTreeRegressor, export_text

data = {
    "Mileage": [15000, 30000, 45000, 60000, 75000, 90000, 120000, 20000],
    "Age": [1, 2, 3, 4, 5, 6, 8, 2],
    "Brand": [1, 1, 2, 2, 3, 3, 4, 1],
    "Engine": [2.0, 1.8, 2.0, 1.5, 1.6, 1.5, 1.2, 2.0],
    "Price": [28000, 25000, 22000, 18000, 15000, 12000, 8000, 27000]
}

df = pd.DataFrame(data)

X = df[["Mileage", "Age", "Brand", "Engine"]]
y = df["Price"]

model = DecisionTreeRegressor(max_depth=4, random_state=42)
model.fit(X, y)

mileage = float(input("Enter mileage: "))
age = float(input("Enter car age: "))
brand = float(input("Enter brand code: "))
engine = float(input("Enter engine size: "))

prediction = model.predict([[mileage, age, brand, engine]])

print("Predicted Car Price:", round(prediction[0], 2))

print("\nDecision Path:")
print(export_text(model, feature_names=list(X.columns)))
