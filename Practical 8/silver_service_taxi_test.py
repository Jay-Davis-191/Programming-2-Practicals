"""CP1404 Practical 8
    silver_service_taxi_test.py
    By Jay Davis"""


from Taxi import SilverService


def main():
    """Demo test code to show how to use car class."""
    import random
    fanciness_rating = random.uniform(0, 5)
    Car = SilverService("Prius 1", 100, fanciness_rating)
    Car.start_fare()
    Car.drive(40)
    print(Car.__str__())
    print("Total fare: $" + "{:.2f}".format(Car.get_fare()))
    Car.start_fare()
    Car.drive(100)
    print(Car.__str__())
    print("Total fare: $" + "{:.2f}".format(Car.get_fare()))


main()
