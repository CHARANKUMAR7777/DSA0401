import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

X = np.array([
    [1000, 10, 20],
    [1200, 12, 25],
    [1500, 15, 30],
    [5000, 40, 100],
    [5500, 45, 110],
    [6000, 50, 120],
    [800, 8, 15],
    [900, 9, 18],
    [5200, 42, 105]
])

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

model.fit(X_scaled)

print("Customer Segments:")

for i, cluster in enumerate(model.labels_):
    print("Customer", i + 1, "-> Segment", cluster)

spending = float(input("Enter Annual Spending: "))
visits = float(input("Enter Visits Per Year: "))
items = float(input("Enter Items Purchased: "))

new_customer = scaler.transform(
    [[spending, visits, items]]
)

segment = model.predict(new_customer)

print("New Customer Segment:", segment[0])
