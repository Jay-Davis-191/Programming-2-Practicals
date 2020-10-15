"""CP1404 Practical 8
    Taxi_test.py
    By Jay Davis"""


from Taxi import Taxi


def main():
    """Demo test code to show how to use car class."""
    Car = Taxi("Prius 1", 100)
    Car.start_fare()
    Car.drive(40)
    print(Car.__str__())
    print("Total fare: $" + "{:.2f}".format(Car.get_fare()))
    Car.start_fare()
    Car.drive(100)
    print(Car.__str__())
    print("Total fare: $" + "{:.2f}".format(Car.get_fare()))


main()
