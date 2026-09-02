import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

data = {
    "Age": [25, 30, 35, 40, 45, 50, 55, 60, 28, 38, 48, 58, 32, 42, 52],
    "Gender": [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    "BloodPressure": [110, 120, 115, 130, 125, 140, 135, 145,
                      118, 128, 138, 142, 122, 132, 136],
    "Cholesterol": [170, 180, 165, 210, 190, 230, 220, 240,
                    175, 200, 215, 225, 185, 195, 205],
    "Outcome": ["Good", "Good", "Good", "Bad", "Good", "Bad", "Bad",
                "Bad", "Good", "Good", "Bad", "Bad", "Good", "Bad", "Bad"]
}

df = pd.DataFrame(data)

X = df[["Age", "Gender", "BloodPressure", "Cholesterol"]]
y = df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, pos_label="Good"))
print("Recall:", recall_score(y_test, y_pred, pos_label="Good"))
print("F1 Score:", f1_score(y_test, y_pred, pos_label="Good"))

print("\nActual vs Predicted:")
print(pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
}))
