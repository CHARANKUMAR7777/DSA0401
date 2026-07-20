fuel = [25, 30, 28, 35, 32]

average = sum(fuel) / len(fuel)

improvement = ((fuel[3] - fuel[0]) / fuel[0]) * 100

print("Average Fuel Efficiency:", average)
print("Percentage Improvement:", improvement, "%")
