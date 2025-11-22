"""
CP1404/CP5632 Practical
Unreliable_car class
"""
from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car, only sometimes, based on reliability."""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven