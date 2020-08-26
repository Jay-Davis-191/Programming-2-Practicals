def convert_to_fahrenheit(temperature):
    number = (temperature * 9 / 5) + 32
    return number

def convert_to_celsius(temperature):
    number = (temperature - 32) * 5 / 9
    return number

def valid_option(choice):
    if option == "C" or option == "c" or option == "F" or option == "f":
        return True
    else:
        return False


option = input("Which temperature: C or F? ")
valid_option(option)
temperature = float(input("What is the temperature: "))
if option == "C" or option == "c":
    fahrenheit = convert_to_fahrenheit(temperature)
    print("{}'F".format(fahrenheit))
elif option == "F" or option == "f":
    celsius = convert_to_celsius(temperature)
    print("{}'C".format(celsius))

