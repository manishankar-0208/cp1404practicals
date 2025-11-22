"""
CP1404/CP5632 Practical
Taxi Simulator Program
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    print("Let's drive!")
    taxis = []
    taxis.append(Taxi("Prius", 100))
    taxis.append(SilverServiceTaxi("Limo", 100, 2))
    taxis.append(SilverServiceTaxi("Hummer", 200, 4))

    bill_to_date = 0
    current_taxi = None

    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                bill_to_date += drive_taxi(current_taxi)
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    """Display the list of taxis and return the selected one."""
    print("Taxis available:")
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        if taxi_choice < 0 or taxi_choice >= len(taxis):
            print("Invalid taxi choice")
            return None
        return taxis[taxi_choice]
    except ValueError:
        print("Invalid taxi choice")
        return None


def drive_taxi(taxi):
    """Drive the selected taxi and return the trip fare."""
    try:
        distance = float(input("Drive how far? "))
    except ValueError:
        print("Invalid distance")
        return 0

    taxi.start_fare()
    taxi.drive(distance)
    fare = taxi.get_fare()
    print(f"Your {taxi.name} trip cost you ${fare:.2f}")
    return fare


def display_taxis(taxis):
    """Print all available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == "__main__":
    main()
