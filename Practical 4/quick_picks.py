"""
CP1404 Programming 2
Jay Davis Practical 4
"""

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBER_EACH_LINE = 6



# Program to generate number of random quick picks, given by the user
def main(number_of_picks):
    quick_pick_list = []
    for x in range(NUMBER_EACH_LINE):
        import random
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in quick_pick_list:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_pick_list.append(number)

    quick_pick_list_sorted = sorted(quick_pick_list)
    print("  ".join(map(str, quick_pick_list_sorted)))





number_of_picks = int(input("How many quick picks? "))
for x in range(number_of_picks):
    main(number_of_picks)
