def main():
    """Perform various list operations."""
    numbers = get_numbers()
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.2f}")


def get_numbers():
    """Get a list of numbers from the user."""
    numbers = []
    for i in range(5):
        number = int(input(f"Enter number {i + 1}: "))
        numbers.append(number)
    return numbers


def check_user_access():
    """Check if the username is valid for access."""
    valid_usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
                       'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    username = input("Enter your username: ")
    if username in valid_usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
check_user_access()
