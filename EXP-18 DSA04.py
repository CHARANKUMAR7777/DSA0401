# Number of likes received by each post
likes = [120, 250, 120, 300, 250, 120, 450, 300, 250, 500, 120]

# Create an empty dictionary
frequency = {}

# Calculate frequency distribution
for like in likes:
    if like in frequency:
        frequency[like] += 1
    else:
        frequency[like] = 1

# Display results
print("Frequency Distribution of Likes\n")

for like in sorted(frequency):
    print("Likes", like, ":", frequency[like])
