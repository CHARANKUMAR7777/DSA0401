house_data = [
    [3, 1500, 250000],
    [5, 2200, 450000],
    [6, 3000, 600000],
    [4, 1800, 320000],
    [5, 2500, 500000]
]

total = 0
count = 0

for house in house_data:
    if house[0] > 4:
        total += house[2]
        count += 1

average = total / count

print("Average Sale Price:", average)
