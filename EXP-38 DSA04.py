import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    "Annual_Spending": [500, 700, 800, 1200, 1500,
                        3000, 3500, 4000, 6000, 7000],

    "Purchases": [5, 7, 8, 12, 15, 25, 30, 35, 45, 50],

    "Website_Visits": [20, 25, 30, 40, 45,
                       70, 80, 90, 120, 130]
}

df = pd.DataFrame(data)

X = df[[
    "Annual_Spending",
    "Purchases",
    "Website_Visits"
]]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["Cluster"] = model.fit_predict(X_scaled)

print("Customer Segmentation:")
print(df)

plt.scatter(
    df["Annual_Spending"],
    df["Purchases"],
    c=df["Cluster"]
)

plt.xlabel("Annual Spending")
plt.ylabel("Number of Purchases")
plt.title("Customer Segmentation")

plt.show()
