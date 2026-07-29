from collections import Counter
import string

# Customer reviews
reviews = [
    "This product is excellent",
    "Excellent quality and excellent service",
    "Good product and good value",
    "Service is very good"
]

# Combine all reviews into one string
text = " ".join(reviews).lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Split text into words
words = text.split()

# Calculate frequency distribution
frequency = Counter(words)

# Display frequency distribution
print("Word Frequency Distribution\n")

for word, count in frequency.items():
    print(word, ":", count)
