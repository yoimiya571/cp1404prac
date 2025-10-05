# Task 1: Write user's name to a file
name = input("Enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)

# Task 2: Read name from file and print greeting
with open("name.txt", "r") as file:
    name_in_file = file.read().strip()  # Using read() to get the whole file content
    print(f"Hi {name_in_file}!")

# Task 3: Read first two numbers from numbers.txt and print their sum
with open("numbers.txt", "r") as file:
    first_number = int(file.readline().strip())  # Using readline() to read the first line
    second_number = int(file.readline().strip())  # Using readline() to read the second line
    print(first_number + second_number)  # Should print 59

# Task 4: Calculate the total sum of all numbers in numbers.txt
with open("numbers.txt", "r") as file:
    total = 0
    for line in file:  # Using for line in file to read all lines
        total += int(line.strip())
    print(total)
