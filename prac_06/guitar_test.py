"""
CP1404/CP5632 Practical - Client code to use the guitar class.
Estimate: 10 minutes
Actual:   10 minutes
"""

from prac_06.guitar import Guitar


def run_tests():
    """Demo test code to show how to use the Guitar class."""
    guitar = Guitar("Gibson L-5 CES", 1960, 16035.40)
    other = Guitar("Another Guitar", 2012, 1512.9)

    print(f"{guitar.name} get_age() - Expected {3}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {13}. Got {other.get_age()}")
    print()
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()}")


if __name__ == '__main__':
    run_tests()