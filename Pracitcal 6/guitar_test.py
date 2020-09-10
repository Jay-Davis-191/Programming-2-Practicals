"""CP1404 Practical - Uses guitar class"""

print("My guitars!")
from guitars import Guitar

"""The program should use a list to store all of the user's guitars (keep inputting until they enter a blank name), then print their details."""

guitar = Guitar()
condition = Guitar.get_condition(self=guitar)
while condition == True:
    guitar = Guitar.get_other_details(self=guitar)
    guitar = Guitar()
    condition = Guitar.get_condition(self=guitar)


guitar.print_details()
