"""
CP1404 - Jay Davis Practical
Program to obtain score from user and input their score
"""

def main(number):
    if number > 100:
        return "Invalid score"
    elif number >= 90:
        return "Excellent"
    elif number >= 50:
        return "Passable"
    else:
        return "Bad"


score = float(input("Score: "))
score_converted = main(score)
print(score_converted)
print("Your score was {:,.0f} which is {}.".format(score, score_converted))


import rando
random_score = random.randint(0, 101)
random_score_converted = main(random_score)
print("A random score is {:,.0f} which is {}.".format(random_score, random_score_converted))
