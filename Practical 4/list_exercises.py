"""
CP1404 Programming 2
Jay Davis Practical 4
"""

number_list = []
MAX_NUMBERS = 5
FIRST_NUMBER = 0
LAST_NUMBER = MAX_NUMBERS - 1

def main():
    for i in range(MAX_NUMBERS):
        number = int(input("Number: "))
        number_list.append(number)

main()
print(number_list[FIRST_NUMBER])
print(number_list[LAST_NUMBER])
number_list.sort()
print(min(number_list))
print(max(number_list))
average = sum(number_list)/5
print(average)

"""--------------------------------------------------------------------------------------------------------------------------"""

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
answer = input("Username: ")
if answer in usernames:
    print("Access Granted!")
else:
    print("Access Denied!")

"""--------------------------------------------------------------------------------------------------------------------------"""

"""
CP1404/CP5632 Practical
List comprehensions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing",
              "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# list comprehension that does the same thing as the loop above
first_initials = [name[0] for name in names]
print(first_initials)

# list comprehension that creates a list containing the initials
# splits each name and adds the first letters of each part to a string
full_initials = [name.split()[0][0] + name.split()[1][0] for name in
                 full_names]
print(full_initials)

# one more example, using filtering to select only the names that start with A
a_names = [name for name in names if name.startswith('A')]
print(a_names)

# TODO: use a list comprehension to create a list of all of the full_names
# in lowercase format
lowercase_full_names = [names.lower() for names in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
# TODO: use a list comprehension to create a list of integers
# from the above list of strings
numbers = list(map(int, almost_numbers))
print(numbers)

greater_numbers = []
# TODO: use a list comprehension to create a list of only the numbers that are
# greater than 9 from the numbers (not strings) you just created
for i in numbers:
    if i > 9:
        greater_numbers.append(i)
print(greater_numbers)
