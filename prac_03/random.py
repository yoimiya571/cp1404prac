import random

# Generate a random integer between 5 and 20 inclusive.
print(random.randint(5, 20))  # line 1

# Generate a random odd number between 3 and 9 inclusive.
print(random.randrange(3, 10, 2))  # line 2

# Generate a random floating-point number between 2.5 and 5.5.
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# Smallest: 5, Largest: 20

# What did you see on line 2?
# Smallest: 3, Largest: 9
# Line 2 could not produce a 4 because the step is 2, generating only odd numbers: 3, 5, 7, or 9.

# What did you see on line 3?
# Smallest: 2.5, Largest: 5.5

# Code to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
