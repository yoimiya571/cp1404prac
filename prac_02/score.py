"""Program to determine grade result based on score."""

import random

def main():
    """Main function to get user score and print the result."""
    score = int(input("Enter score (0-100): "))
    result = determine_result(score)
    print(f"Your result is: {result}")

    # Generate random score and print result
    random_score = random.randint(0, 100)
    random_result = determine_result(random_score)
    print(f"Random score {random_score} is: {random_result}")

def determine_result(score):
    """Return grade result string based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"

if __name__ == "__main__":
    main()
