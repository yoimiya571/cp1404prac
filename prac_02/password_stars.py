"""password_stars.py

A program that prompts user for a password and prints asterisks corresponding to the length of the password.
Refactored to use functions and follow SRP.
"""

MIN_PASSWORD_LENGTH = 5

def main():
    """Main function to run password check and print stars."""
    password = get_password()
    print_stars(password)


def get_password():
    """Prompt user for password until it meets minimum length requirement. Return the password."""
    while True:
        password = input(f"Enter a password of at least {MIN_PASSWORD_LENGTH} characters: ")
        if len(password) >= MIN_PASSWORD_LENGTH:
            return password
        print(f"Password must be at least {MIN_PASSWORD_LENGTH} characters long.")


def print_stars(password, symbol='*'):
    """Print a line of symbols with the same length as the password.

    Args:
        password (str): The password string.
        symbol (str, optional): The symbol to print. Defaults to '*'.
    """
    print(symbol * len(password))


if __name__ == "__main__":
    main()
