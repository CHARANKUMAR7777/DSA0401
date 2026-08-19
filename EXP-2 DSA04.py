#companysales 
    [100, 120, 110],
    [200, 190, 210],
    [150, 160, 170]
]

total = 0
count = 0

for row in sales:
    for price in row:
        total += price
        count += 1

average = total / count

print("Average Price:", average)
