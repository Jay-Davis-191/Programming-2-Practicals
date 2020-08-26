"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MAX_LENGTH = 10

def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be {} or less characters:".format(MAX_LENGTH))
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password), password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    length = 0
    for char in password:
        length += 1
        pass

    if length == 0 or length > MAX_LENGTH:
        return False
    else:
        return True

main()