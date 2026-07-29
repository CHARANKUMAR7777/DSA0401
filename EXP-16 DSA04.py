from collections import Counter
import string

# Sample paragraph
text = """
Python is a powerful programming language.
Python is easy to learn.
Data analysis using Python is interesting.
"""

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Split into words
words = text.split()

# Frequency distribution
frequency = Counter(words)

print("Word Frequency Distribution:\n")
for word, count in frequency.items():
    print(word, ":", count)

print("\nTop 10 Most Frequent Words")
print(frequency.most_common(10))
