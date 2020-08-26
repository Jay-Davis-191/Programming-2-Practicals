"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MAX_LENGTH = 10

def main():
    """Program to check validity of password"""
    print("Please enter a valid password")
    print("Password must be less than {} characters.".format(MAX_LENGTH))
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password")
        password = input("> ")
    print = ("Your {} charcter password is valid: {}".format(len(pasword), password))

def is_valid_password(password):
    lwength = 0
    for char in password:
        length += 1
    if length == 0 or length > 10:
        return False
    else:
        return True

main()
