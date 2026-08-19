import math

# Conversion rates (%) for Website Design A
design_A = [12, 14, 13, 15, 16, 14, 13, 15, 14, 16]

# Conversion rates (%) for Website Design B
design_B = [18, 17, 19, 18, 20, 19, 18, 17, 19, 20]

# Function to calculate mean
def mean(data):
    return sum(data) / len(data)

# Function to calculate sample variance
def variance(data):
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / (len(data) - 1)

# Calculate statistics
n1 = len(design_A)
n2 = len(design_B)

mean1 = mean(design_A)
mean2 = mean(design_B)

var1 = variance(design_A)
var2 = variance(design_B)

# Pooled variance
pooled = ((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2)

# t-statistic
t = (mean1 - mean2) / math.sqrt(pooled * (1/n1 + 1/n2))

print("Mean of Design A =", round(mean1, 2))
print("Mean of Design B =", round(mean2, 2))
print("t-statistic =", round(t, 3))

# Decision
critical_t = 2.101   # 95% confidence, df = 18

if abs(t) > critical_t:
    print("\nResult:")
    print("There is a statistically significant difference between Design A and Design B.")
else:
    print("\nResult:")
    print("There is NO statistically significant difference between Design A and Design B.")
