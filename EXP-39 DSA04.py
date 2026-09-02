import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    "Customer_ID": [
        "C01", "C02", "C03", "C04", "C05",
        "C06", "C07", "C08", "C09", "C10"
    ],

    "Total_Spent": [
        500, 700, 900, 1500, 1800,
        3500, 4000, 4500, 6000, 7000
    ],

    "Visits": [
        5, 7, 8, 12, 15,
        25, 30, 32, 40, 45
    ]
}

df = pd.DataFrame(data)

X = df[["Total_Spent", "Visits"]]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["Cluster"] = model.fit_predict(X_scaled)

print("Customer Segments:")
print(df)

plt.scatter(
    df["Total_Spent"],
    df["Visits"],
    c=df["Cluster"]
)

plt.xlabel("Total Amount Spent")
plt.ylabel("Frequency of Visits")
plt.title("Customer Spending Segments")

plt.show()
