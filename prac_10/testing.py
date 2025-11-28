"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    # return s * n
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length

def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # Car initialisation tests
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # Should use the value passed in
    car = Car(fuel=10)
    assert car.fuel == 10, "Car fails if it does not set fuel correctly when fuel is provided"

    # Should use the default value (0)
    empty_car = Car()
    assert empty_car.fuel == 0, "Car test fail if it does not set default fuel correctly"

def format_sentence(phrase):
    """
    Format a phrase as a sentence: capital first letter, single period at end.
    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("good morning!")
    'Good morning!'
    """
    sentence = phrase.strip()
    sentence = sentence[0].upper() + sentence[1:]
    if sentence[-1] not in ".!?":
        sentence += "."
    return sentence

def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # Car initialisation tests
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # Should use the value passed in
    car = Car(fuel=10)
    assert car.fuel == 10, "Car does not set fuel correctly when fuel is provided"

    # Should use the default value (0)
    empty_car = Car()
    assert empty_car.fuel == 0, "Car does not set default fuel correctly"

run_tests()
doctest.testmod()
