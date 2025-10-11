import random

def main():
    """Generate quick picks for a lottery."""
    number_of_picks = int(input("How many quick picks? "))
    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in sorted(quick_pick)))


def generate_quick_pick():
    """Generate a quick pick: a set of 6 unique random numbers between 1 and 45."""
    quick_pick = random.sample(range(1, 46), 6)  # Generates 6 unique random numbers in the range 1-45
    return quick_pick


main()