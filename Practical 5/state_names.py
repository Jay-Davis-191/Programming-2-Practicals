"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)
state_code = input("Enter short state: ")

while state_code != "":
    if state_code in CODE_TO_NAME:
        print("{:5} is {:5}".format(state_code, CODE_TO_NAME[state_code]))
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")

for x in CODE_TO_NAME:
    print("{:5} is {:5}".format(x, CODE_TO_NAME[x]))
