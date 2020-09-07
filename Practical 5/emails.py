details = {"lindsay.ward@jcu.edu.au": "Lindsay Ward", "abe@gmail.com": "Abe", "jimbo546@hotmail.com": "Jimbo546"}

email_input = input("Email: ")
while email_input != "":
    if email_input in details:
        response = input("Is your name {}? (Y/N) ".format(details[email_input]))
        response = response.title()
        while response != "N" and response != "No" and response != "Y" and response != "Yes":
            print("Invalid response")
            email_input = input("Email: ")
        if response == "N" or response == "No":
            name = input("Name: ")
            details[email_input] = name.title()
            email_input = input("Email: ")
        elif response == "Y" or response == "Yes":
            email_input = input("Email: ")
    else:
        print("That email is not in our database.")
        email_input = input("Email: ")

longest_name = max(details)

for x in details:
    print("{:{}} ({})".format(x, len(longest_name), details[x]))
