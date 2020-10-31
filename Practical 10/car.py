"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """Represent a Car object."""
    def get_name_of_vehicle(self):
        self.name_of_car = input("What is the name of the vehicle? ")

    def __init__(self, fuel=0):
        """Initialise a Car instance.
        fuel: float, one unit of fuel drives one kilometre
        """
        self.fuel = fuel
        self.odometer = 0

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.
        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance

    def odometer(self):
        return self.odometer

    def fuel(self):
        return self.fuel

    def print_results(self):
        """Prints fuel and odometer readings of vehicle"""
        print("{}, fuel={}, odometer={}\n".format(self.name_of_car, self.fuel, self.odometer))
        
