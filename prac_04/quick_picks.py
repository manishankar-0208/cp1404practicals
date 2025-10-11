"""
CP1404/CP5632 Practical
Quick Picks Generator
"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6


def main():
    """Generate random quick picks for the user."""
    number_of_picks = get_valid_number("How many quick picks? ")

    for i in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print_quick_pick(quick_pick)


def get_valid_number(prompt):
    """Get a valid number from the user."""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(prompt))
            if number > 0:
                is_valid_input = True
                return number
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input! please enter a valid number.")


def generate_quick_pick():
    """Generate one quick pick (6 unique sorted numbers)."""
    numbers = []
    while len(numbers) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers


def print_quick_pick(numbers):
    """Print a quick pick in nicely formatted ascending order."""
    print(" ".join(f"{number:2}" for number in numbers))


main()
