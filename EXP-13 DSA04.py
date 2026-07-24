import csv
import math
import os

filename = "stock_data.csv"

# Create CSV file if it does not exist
if not os.path.exists(filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Day", "Closing_Price"])
        writer.writerow([1,120])
        writer.writerow([2,123])
        writer.writerow([3,121])
        writer.writerow([4,125])
        writer.writerow([5,128])
        writer.writerow([6,127])
        writer.writerow([7,130])
        writer.writerow([8,132])
        writer.writerow([9,131])
        writer.writerow([10,135])

prices = []

# Read data from CSV file
with open(filename, "r") as file:
    reader = csv.reader(file)
    next(reader)   # Skip header

    for row in reader:
        prices.append(float(row[1]))

# Calculate statistics
n = len(prices)
average = sum(prices) / n
variance = sum((x - average) ** 2 for x in prices) / n
std_deviation = math.sqrt(variance)
maximum = max(prices)
minimum = min(prices)

# Display results
print("========== Stock Price Analysis ==========")
print("Number of Trading Days :", n)
print("Average Closing Price  :", round(average, 2))
print("Maximum Price          :", maximum)
print("Minimum Price          :", minimum)
print("Variance               :", round(variance, 2))
print("Standard Deviation     :", round(std_deviation, 2))

if std_deviation > 5:
    print("Insight: High variability in stock prices.")
else:
    print("Insight: Low variability in stock prices.")
