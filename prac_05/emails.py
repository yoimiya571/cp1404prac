def main():
    #Prompt user for emails and print formatted name-email pairs
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm != "" and confirm != "y":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    #Extract name from email address using the part before '@'
    name_part = email.split('@')[0]
    name = name_part.replace('.', ' ').title()
    return name


if __name__ == '__main__':
    main()