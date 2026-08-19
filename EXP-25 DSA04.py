import math

# Customer ratings (Sample Data)
ratings = [4, 5, 3, 4, 5, 4, 5, 3, 4, 5,
           4, 4, 5, 3, 5, 4, 5, 4, 3, 5]

# Number of ratings
n = len(ratings)

# Mean
mean = sum(ratings) / n

# Standard Deviation
variance = sum((x - mean) ** 2 for x in ratings) / (n - 1)
sd = math.sqrt(variance)

# 95% Confidence Interval (Z = 1.96)
z = 1.96
margin = z * (sd / math.sqrt(n))

lower = mean - margin
upper = mean + margin

# Display Results
print("Customer Ratings Analysis")
print("-------------------------")
print("Number of Ratings :", n)
print("Average Rating    :", round(mean, 2))
print("Standard Deviation:", round(sd, 2))
print("95% Confidence Interval")
print("Lower Limit :", round(lower, 2))
print("Upper Limit :", round(upper, 2))
