from collections import Counter
import string

# Customer feedback dataset
feedback = [
    "Great service and fast delivery",
    "Excellent product quality",
    "Fast delivery and good packaging",
    "Good quality product",
    "Excellent customer service",
    "Product is excellent and delivery is fast"
]

# Combine all feedback into one text
text = " ".join(feedback).lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Split text into words
words = text.split()

# Calculate word frequency
frequency = Counter(words)

# Display all word frequencies
print("Word Frequency Distribution\n")

for word, count in frequency.items():
    print(word, ":", count)

# Display top 10 most frequent words
print("\nTop 10 Most Frequent Words\n")

for word, count in frequency.most_common(10):
    print(word, ":", count)
