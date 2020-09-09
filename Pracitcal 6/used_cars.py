"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    my_car.get_name_of_vehicle()
    my_car.print_results()

    my_limo = Car(120)
    my_limo.drive(115)
    my_limo.get_name_of_vehicle()
    my_limo.print_results()


main()
