"""Menu-driven program to handle scores and show results."""

def main():
    """Main menu loop to get score, print result, show stars, or quit."""
    score = get_valid_score()
    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input("Choose an option: ").upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            result = determine_result(score)
            print(f"Result: {result}")
        elif choice == 'S':
            print_stars(score)
        elif choice == 'Q':
            print("Farewell!")
            break
        else:
            print("Invalid option, please choose again.")

def get_valid_score():
    """Prompt user for a valid score between 0 and 100 inclusive."""
    while True:
        try:
            score = int(input("Enter a score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input; enter an integer.")

def determine_result(score):
    """Return the grade result string based on the score."""
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"

def print_stars(score):
    """Print stars corresponding to the score."""
    print('*' * score)

if __name__ == "__main__":
    main()