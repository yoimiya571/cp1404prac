"""Temperature conversion program with functions for Celsius and Fahrenheit."""

def main():
    """Main function to get user input and display converted temperatures."""
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    converted_to_f = celsius_to_fahrenheit(celsius)
    converted_to_c = fahrenheit_to_celsius(fahrenheit)

    print(f"{celsius:.2f}°C is {converted_to_f:.2f}°F")
    print(f"{fahrenheit:.2f}°F is {converted_to_c:.2f}°C")

def celsius_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit temperature to Celsius."""
    return (fahrenheit - 32) * 5 / 9

if __name__ == "__main__":
    main()
