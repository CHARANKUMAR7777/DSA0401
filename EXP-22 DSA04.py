import math

# Sample data (Blood Pressure Reduction)
drug = [12, 15, 14, 16, 13, 18, 17, 14, 15, 16]
placebo = [5, 6, 4, 7, 5, 6, 5, 4, 6, 5]

# Function to calculate mean
def mean(data):
    return sum(data) / len(data)

# Function to calculate standard deviation
def std_dev(data):
    m = mean(data)
    variance = sum((x - m) ** 2 for x in data) / (len(data) - 1)
    return math.sqrt(variance)

# Function to calculate 95% Confidence Interval
def confidence_interval(data):
    n = len(data)
    m = mean(data)
    sd = std_dev(data)

    # Z-value for 95% Confidence Interval
    z = 1.96

    margin = z * (sd / math.sqrt(n))

    lower = m - margin
    upper = m + margin

    return m, lower, upper

# Drug Group
drug_mean, drug_low, drug_high = confidence_interval(drug)

# Placebo Group
placebo_mean, placebo_low, placebo_high = confidence_interval(placebo)

# Display Results
print("Drug Group")
print("Mean =", round(drug_mean, 2))
print("95% Confidence Interval = ({:.2f}, {:.2f})".format(drug_low, drug_high))

print("\nPlacebo Group")
print("Mean =", round(placebo_mean, 2))
print("95% Confidence Interval = ({:.2f}, {:.2f})".format(placebo_low, placebo_high))
