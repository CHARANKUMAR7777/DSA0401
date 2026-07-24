import math

# Temperature data (daily readings for each city)
temperature = {
    "Chennai": [32, 33, 31, 34, 35, 33, 32],
    "Coimbatore": [28, 29, 30, 28, 27, 29, 28],
    "Madurai": [35, 36, 37, 34, 35, 36, 38],
    "Salem": [30, 31, 30, 29, 30, 31, 30]
}

mean_temp = {}
std_dev = {}
temp_range = {}

# Calculate mean, standard deviation, and range
for city, temps in temperature.items():
    n = len(temps)

    mean = sum(temps) / n
    mean_temp[city] = mean

    variance = 0
    for t in temps:
        variance += (t - mean) ** 2
    variance = variance / n

    std = math.sqrt(variance)
    std_dev[city] = std

    temp_range[city] = max(temps) - min(temps)

# Display mean temperature
print("Mean Temperature")
for city in mean_temp:
    print(city, ":", round(mean_temp[city], 2), "°C")

# Display standard deviation
print("\nStandard Deviation")
for city in std_dev:
    print(city, ":", round(std_dev[city], 2))

# City with highest temperature range
highest_range_city = max(temp_range, key=temp_range.get)
print("\nCity with Highest Temperature Range:")
print(highest_range_city, "-", temp_range[highest_range_city], "°C")

# City with most consistent temperature
consistent_city = min(std_dev, key=std_dev.get)
print("\nCity with Most Consistent Temperature:")
print(consistent_city, "-", round(std_dev[consistent_city], 2))
