import math

# Sample rare element concentration data
data = [10.5, 11.2, 9.8, 10.9, 11.5, 10.1, 9.9, 10.8,
        11.0, 10.6, 9.7, 10.4, 11.3, 10.2, 10.7,
        11.1, 10.0, 10.3, 11.4, 10.9]

# User input
sample_size = int(input("Enter sample size: "))
confidence = int(input("Enter confidence level (90/95/99): "))
precision = float(input("Enter desired precision: "))

# Take sample
sample = data[:sample_size]

# Mean
mean = sum(sample) / len(sample)

# Standard deviation
variance = sum((x - mean) ** 2 for x in sample) / (len(sample) - 1)
sd = math.sqrt(variance)

# Z-values
if confidence == 90:
    z = 1.645
elif confidence == 95:
    z = 1.96
elif confidence == 99:
    z = 2.576
else:
    print("Invalid confidence level")
    exit()

# Margin of error
margin = z * (sd / math.sqrt(sample_size))

# Confidence interval
lower = mean - margin
upper = mean + margin

print("\nPoint Estimate (Mean):", round(mean, 2))
print("Standard Deviation:", round(sd, 2))
print("Desired Precision:", precision)
print("95% Confidence Interval:")
print("(", round(lower,2), ",", round(upper,2), ")")
