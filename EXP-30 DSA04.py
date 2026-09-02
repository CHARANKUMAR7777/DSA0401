import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

X = np.array([
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 1]
])

y = np.array([1, 1, 1, 0, 0, 0, 1, 0, 1, 0])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

k = int(input("Enter k value: "))

model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_scaled, y)

fever = int(input("Fever (0/1): "))
cough = int(input("Cough (0/1): "))
fatigue = int(input("Fatigue (0/1): "))
pain = int(input("Body Pain (0/1): "))

patient = scaler.transform([[fever, cough, fatigue, pain]])

prediction = model.predict(patient)

if prediction[0] == 1:
    print("Medical Condition: PRESENT")
else:
    print("Medical Condition: NOT PRESENT")
