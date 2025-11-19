"""
CP1404/CP5632 Practical
SilverServiceTaxi class tests
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Hummer", 200, 4)
    taxi.drive(0)
    print(taxi)
    print(taxi.get_fare())
    taxi = SilverServiceTaxi("Silver Service Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())

main()