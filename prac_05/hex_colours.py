# Dictionary of colour names to hexadecimal codes
COLOUR_NAME_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "Blue": "#0000ff",
    "Coral": "#ff7f50",
    "DarkKhaki": "#bdb76b"
}

# Input loop
colour_name = input("Enter a colour name (or blank to quit): ").strip()
while colour_name != "":
    hex_code = COLOUR_NAME_TO_HEX.get(colour_name.title())
    if hex_code:
        print(f"The hex code for {colour_name} is {hex_code}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter a colour name (or blank to quit): ").strip()
