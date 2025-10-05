import random

# Constants
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "stock_prices.txt"

# Initialize variables
price = INITIAL_PRICE
number_of_days = 0

# Open file for writing
out_file = open(FILENAME, 'w')

# Print and write the starting price to the file
print(f"Starting price: ${price:,.2f}")
print(f"Starting price: ${price:,.2f}", file=out_file)

# Main loop to simulate price changes
while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1
    price_change = 0

    # Determine if the price increases or decreases
    if random.randint(1, 2) == 1:
        # Price increases
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # Price decreases
        price_change = random.uniform(-MAX_DECREASE, 0)

    # Apply the price change
    price *= (1 + price_change)

    # Print and write the updated price with the number of days
    print(f"On day {number_of_days} price is: ${price:,.2f}")
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# Close the file after the loop ends
out_file.close()
