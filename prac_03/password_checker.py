"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)

    # Get user input and validate the password
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")

    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # Check if the password length is within the allowed range
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0

    # Loop through each character and count types
    for character in password:
        if character.islower():
            number_of_lower += 1
        elif character.isupper():
            number_of_upper += 1
        elif character.isdigit():
            number_of_digit += 1
        elif character in SPECIAL_CHARACTERS:
            number_of_special += 1

    # Check if password contains at least one of each required character type
    if number_of_lower == 0 or number_of_upper == 0 or number_of_digit == 0:
        return False

    # If special characters are required, check the count of those
    if IS_SPECIAL_CHARACTER_REQUIRED and number_of_special == 0:
        return False

    # If we passed all checks, the password is valid
    return True


main()
