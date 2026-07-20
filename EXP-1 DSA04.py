student_scores = [
    [85, 78, 90, 88],
    [92, 80, 86, 91],
    [76, 85, 84, 79],
    [89, 90, 92, 87]
]

subjects = ["Math", "Science", "English", "History"]

averages = []

for col in range(4):
    total = 0
    for row in range(4):
        total += student_scores[row][col]
    averages.append(total / 4)

print("Average Scores:")
for i in range(4):
    print(subjects[i], ":", averages[i])

highest = averages.index(max(averages))
print("Highest Average Subject:", subjects[highest])
