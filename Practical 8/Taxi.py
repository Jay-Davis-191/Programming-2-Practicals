"""CP1404 Practical 8
    Taxi.py
    By Jay Davis"""


class Taxi:
    price_per_km = 1.23

    """Specialised version of a Car that includes fare costs."""
    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on parent class Car."""
        self.name = name
        self.fuel = fuel
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, {}km on current fare, ${:.2f}/km".format(self.name,
                                                             self.current_fare_distance,
                                                             self.price_per_km)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0
        return self.current_fare_distance

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        self.current_fare_distance += distance
        return distance


class UnreliableCar(Taxi):
    price_per_km = 1.23

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return super().__str__()

    def get_fare(self):
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        self.current_fare_distance = 0
        return self.current_fare_distance

    def drive(self, distance):
        import random
        drive_chance = random.uniform(0, 100)
        """reliability has to be greater than drive_chance for "if" statement to work"""
        if drive_chance > self.reliability:
            distance = 0
        else:
            super().drive(distance)
        return distance


class SilverService(Taxi):
    price_per_km = 1.23

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness

    def __str__(self):
        return "{}, {}km on current fare, ${:.2f}/km".format(self.name,
                                                             self.current_fare_distance,
                                                             (self.price_per_km * self.fanciness))

    def get_fare(self):
        self.upgraded_price_per_km = self.price_per_km * self.fanciness
        return (self.upgraded_price_per_km * self.current_fare_distance) + 4.50

    def start_fare(self):
        self.current_fare_distance = 0
        return self.current_fare_distance

    def drive(self, distance):
        super().drive(distance)
