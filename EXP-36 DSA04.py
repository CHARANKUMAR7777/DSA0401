import numpy as np
from sklearn.linear_model import LogisticRegression

X = np.array([
    [100, 12, 50],
    [150, 24, 45],
    [300, 6, 80],
    [350, 3, 90],
    [120, 24, 40],
    [400, 2, 100],
    [200, 12, 60],
    [450, 1, 110],
    [180, 18, 55],
    [500, 1, 120]
])

y = np.array([0, 0, 1, 1, 0, 1, 0, 1, 0, 1])

model = LogisticRegression()
model.fit(X, y)

usage = float(input("Enter Usage Minutes: "))
contract = float(input("Enter Contract Duration: "))
charges = float(input("Enter Monthly Charges: "))

new_customer = [[usage, contract, charges]]

prediction = model.predict(new_customer)
probability = model.predict_proba(new_customer)

if prediction[0] == 1:
    print("Prediction: Customer WILL CHURN")
else:
    print("Prediction: Customer WILL NOT CHURN")

print("Churn Probability:",
      round(probability[0][1] * 100, 2), "%")
