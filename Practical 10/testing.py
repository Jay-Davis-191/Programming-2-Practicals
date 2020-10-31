"""Practical 10
CP1404 Programming II
Jay Davis """

import doctest
from car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    output = " ".join([str(s)] * n)
    return output


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


def format_sentence(sentence):
    if "." not in sentence:
        sentence += "."
    sentence = sentence.capitalize()
    return sentence


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"
    assert test_car.fuel == 0
    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    test_car = Car(fuel=10)
    assert test_car.fuel == 10
    assert test_car.odometer == 0

    assert format_sentence("hello") == "Hello."
    assert format_sentence("it is an ex parrot.") == "It is an ex parrot."
    assert format_sentence("hope this works") == "Hope this works."


run_tests()

doctest.testmod()

# and one more you decide (one that is valid!)
# test this and watch the tests fail
# then write the body of the function so that the tests pass
