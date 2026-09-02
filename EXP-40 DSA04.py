import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    "Customer_ID": [
        "C101", "C102", "C103", "C104",
        "C105", "C106", "C107", "C108",
        "C109", "C110", "C111", "C112"
    ],

    "Total_Spent": [
        300, 500, 700, 1200, 1500, 1800,
        3000, 3500, 4500, 5000, 6500, 7500
    ],

    "Items_Purchased": [
        3, 5, 7, 10, 12, 15,
        25, 30, 40, 45, 55, 65
    ]
}

df = pd.DataFrame(data)

X = df[["Total_Spent", "Items_Purchased"]]

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

centers = scaler.inverse_transform(
    model.cluster_centers_
)

print("\nCluster Centers:")
print(centers)

plt.scatter(
    df["Total_Spent"],
    df["Items_Purchased"],
    c=df["Cluster"]
)

plt.scatter(
    centers[:, 0],
    centers[:, 1],
    marker="X",
    s=200
)

plt.xlabel("Total Amount Spent")
plt.ylabel("Number of Items Purchased")
plt.title("K-Means Customer Segmentation")

plt.show()
