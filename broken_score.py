"""
CP1404 - Jay Davis Practical
Program to obtain score from user and input their score
"""

def main():
    number = float(input("Score: "))
    return number




score = main()
print("Your score was {:,.0f}.".format(score))

import random

random_number = random.random()
print("A random number is {:,.2f}.".format(random_number))