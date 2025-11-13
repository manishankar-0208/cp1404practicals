"""
CP1404/CP5632 Practical - Client code for Guitar class.
Read guitars from file, display, sort, allow user to add, and save back to file.
Estimate: 15 minutes
Actual:   15 minutes
"""

from prac_07.guitar import Guitar


def main():
    """Read guitars from file, display them, add new ones, then save all."""
    guitars = load_guitars("guitars.csv")
    print("These are my guitars:")
    display_guitars(guitars)

    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    guitars += get_new_guitars()

    save_guitars("guitars.csv", guitars)
    print("\nAll guitars have been saved to guitars.csv.")


def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            name = parts[0]
            year = parts[1]
            cost = parts[2]
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """Display all guitars in a formatted list."""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


def get_new_guitars():
    """Ask user for new guitars and return them as a list of Guitar objects."""
    new_guitars = []
    print("\nEnter new guitars:")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        new_guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")
    return new_guitars


def save_guitars(filename, guitars):
    """Save all guitars to the CSV file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == "__main__":
    main()
