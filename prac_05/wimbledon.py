"""
Wimbledon Champions
Estimate: 30 minutes
Actual:   40 minutes
"""

def read_wimbledon_data(filename):
    """Read the Wimbledon data from a CSV file and return a list of champions."""
    champions = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            champions.append((parts[0], parts[1]))  # (Champion, Country)
    return champions

def count_champions(champions):
    """Count how many times each champion has won."""
    champion_count = {}
    for champion, _ in champions:
        if champion in champion_count:
            champion_count[champion] += 1
        else:
            champion_count[champion] = 1
    return champion_count

def get_countries(champions):
    """Get a set of unique countries that have won Wimbledon."""
    countries = {country for _, country in champions}
    return sorted(countries)

def main():
    """Main function to execute the program."""
    filename = 'wimbledon.csv'
    champions = read_wimbledon_data(filename)

    # Count champions and display results
    champion_count = count_champions(champions)
    print("Wimbledon Champions:")
    for champion, count in sorted(champion_count.items()):
        print(f"{champion} {count}")

    # Get and display countries
    countries = get_countries(champions)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(countries))

if __name__ == "__main__":
    main()