"""CP1404 Practical 8
    unreliable_car.py
    By Jay Davis"""


from Taxi import UnreliableCar


def main():
    """Demo test code to show how to use car class."""
    import random
    chance = random.uniform(0, 100)
    Car = UnreliableCar("Prius 1", 100, chance)
    Car.start_fare()
    Car.drive(40)
    print(Car.__str__())
    print("Total fare: $" + "{:.2f}".format(Car.get_fare()))
    Car.start_fare()
    Car.drive(100)
    print(Car.__str__())
    print("Total fare: $" + "{:.2f}".format(Car.get_fare()))


main()
