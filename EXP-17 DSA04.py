# Customer ages
ages = [22, 25, 30, 25, 22, 35, 30, 25, 28, 22]

# Create an empty dictionary
frequency = {}

# Count frequency of each age
for age in ages:
    if age in frequency:
        frequency[age] += 1
    else:
        frequency[age] = 1

# Display frequency distribution
print("Frequency Distribution of Customer Ages\n")

for age in sorted(frequency):
    print("Age", age, ":", frequency[age])
