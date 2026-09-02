import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = {
    "Size": [800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2500, 2800],
    "Price": [120, 150, 180, 210, 240, 280, 310, 340, 390, 450]
}

df = pd.DataFrame(data)

X = df[["Size"]]
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

size = float(input("Enter house size: "))

prediction = model.predict([[size]])

print("Predicted House Price:", round(prediction[0], 2))

plt.scatter(df["Size"], df["Price"])
plt.plot(df["Size"], model.predict(df[["Size"]]))

plt.xlabel("House Size")
plt.ylabel("House Price")
plt.title("House Size vs House Price")
plt.show()
