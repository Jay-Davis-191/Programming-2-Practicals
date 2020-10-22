"""
CP1404 Practical 9
By Jay Davis
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('FilesToSort')

    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    for filename in os.listdir('.'):
        # Ignore directories, just process files
        file_name, file_extension = os.path.splitext(filename)
        file_extension = file_extension[1:]

        if os.path.exists('temp/' + file_extension):
            shutil.move(filename, 'temp/' + file_extension + '/' + filename)

            # This will create a new directory,
            # if the directory does not already exist
        else:
            os.makedirs('temp/' + file_extension)
            shutil.move(filename, 'temp/' + file_extension + '/' + filename)

main()
