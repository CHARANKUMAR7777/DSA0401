from statistics import mean, median, stdev

# Data of 18 adults
age = [23, 25, 27, 30, 32, 35, 37, 40, 42, 45, 48, 50, 52, 55, 58, 60, 62, 65]
fat = [12, 15, 14, 18, 20, 22, 21, 25, 24, 28, 30, 31, 33, 35, 36, 38, 40, 42]

print("AGE")
print("Mean =", mean(age))
print("Median =", median(age))
print("Standard Deviation =", round(stdev(age), 2))

print("\nBODY FAT (%)")
print("Mean =", mean(fat))
print("Median =", median(fat))
print("Standard Deviation =", round(stdev(fat), 2))
