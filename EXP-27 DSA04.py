import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Lionel","Kevin","Erling","Mohamed","Harry","Bruno","Jude",
             "Vinicius","Rodri","Son","Salah","Saka","Pedri","Rashford","Kane"],
    "Age": [36,32,25,31,30,29,21,23,27,31,30,22,21,26,30],
    "Position": ["Forward","Midfielder","Forward","Forward","Forward",
                 "Midfielder","Midfielder","Forward","Midfielder",
                 "Forward","Forward","Forward","Midfielder","Forward","Forward"],
    "Goals": [25,18,32,28,27,15,12,30,8,20,26,17,7,14,24],
    "Weekly_Salary": [900000,850000,700000,650000,600000,450000,300000,
                      500000,550000,400000,620000,280000,250000,350000,580000]
}

pd.DataFrame(data).to_csv("soccer_players.csv", index=False)

df = pd.read_csv("soccer_players.csv")

print("Top 5 Players by Goals:")
print(df.nlargest(5, "Goals")[["Name", "Goals"]])

print("\nTop 5 Players by Salary:")
print(df.nlargest(5, "Weekly_Salary")[["Name", "Weekly_Salary"]])

average_age = df["Age"].mean()
print("\nAverage Age:", average_age)

print("\nPlayers Above Average Age:")
print(df[df["Age"] > average_age][["Name", "Age"]])

df["Position"].value_counts().plot(kind="bar")
plt.title("Players by Position")
plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.show()
