import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Area": [800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2500, 2800],
    "Bedrooms": [2, 2, 3, 3, 3, 4, 4, 4, 5, 5],
    "Price": [120000, 150000, 180000, 210000, 240000,
              280000, 310000, 340000, 390000, 450000]
}

df = pd.DataFrame(data)

X = df[["Area", "Bedrooms"]]
y = df["Price"]

model = LinearRegression()
model.fit(X, y)

area = float(input("Enter house area: "))
bedrooms = int(input("Enter number of bedrooms: "))

prediction = model.predict([[area, bedrooms]])

print("Predicted House Price:", round(prediction[0], 2))
