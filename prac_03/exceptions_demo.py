"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   - A ValueError will occur if the user enters a non-integer value (e.g., a string or a float) when prompted for the numerator or denominator.

2. When will a ZeroDivisionError occur?
   - A ZeroDivisionError will occur if the user enters 0 as the denominator because division by zero is not allowed.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   - Yes, the code can be changed to check if the denominator is zero before performing the division.
     If it is zero, the program can prompt the user to enter a non-zero denominator.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Check if denominator is zero and prompt the user again if necessary
    while denominator == 0:
        print("Denominator cannot be zero! Please enter a valid denominator.")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
