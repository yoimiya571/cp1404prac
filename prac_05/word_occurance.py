"""
Word Occurrences
Estimate: 30 minutes
Actual:   45 minutes
"""

# Ask the user for input
text = input("Enter a string: ")

# Split the string into words
words = text.split()

# Create a dictionary to count occurrences
word_count = {}

# Count the occurrences of each word
for word in words:
    word = word.lower()  # Convert to lowercase for case insensitivity
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Sort the dictionary by word
sorted_word_count = dict(sorted(word_count.items()))

# Find the longest word length for formatting
max_length = max(len(word) for word in sorted_word_count)

# Print the word counts aligned
for word, count in sorted_word_count.items():
    print(f"{word:{max_length}} : {count}")