"""
CP1404 Practical 9
By Jay Davis
"""
import shutil
import os

file_extension_list = []
file_location_list = []

def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('FilesToSort')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    for filename in os.listdir('.'):
        file_name, file_extension = os.path.splitext(filename)
        file_extension = file_extension[1:]
        location = input("What category would you like to sort {} files into? ".format(file_extension))

        if os.path.exists('temp/' + location):
            shutil.move(filename, 'temp/' + location + '/' + filename)
        else:
            os.makedirs('temp/' + location)
            shutil.move(filename, 'temp/' + location + '/' + filename)


main()
