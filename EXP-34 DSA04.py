import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = {
    "Engine_Size": [1.2, 1.5, 1.6, 1.8, 2.0, 2.2, 2.5, 3.0, 3.5, 4.0],
    "Horsepower": [80, 100, 110, 130, 150, 170, 200, 250, 300, 350],
    "Fuel_Efficiency": [20, 18, 18, 16, 15, 14, 13, 11, 10, 8],
    "Price": [10000, 13000, 15000, 18000, 22000,
              26000, 32000, 40000, 50000, 65000]
}

df = pd.DataFrame(data)

X = df[["Engine_Size", "Horsepower", "Fuel_Efficiency"]]
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

print("\nFeature Influence:")

for feature, coefficient in zip(X.columns, model.coef_):
    print(feature, ":", coefficient)

engine = float(input("Enter Engine Size: "))
hp = float(input("Enter Horsepower: "))
fuel = float(input("Enter Fuel Efficiency: "))

prediction = model.predict([[engine, hp, fuel]])

print("Predicted Car Price:", round(prediction[0], 2))
