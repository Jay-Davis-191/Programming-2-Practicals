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
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        new_name = get_fixed_filename(filename)

        if "_" not in new_name:
            new_name = check_uppercase_lowercase(new_name)
            print("Renaming {} to ".format(filename), end=''),
            for x in new_name:
                if ".txt" in x:
                    print(x)
                else:
                    print(x, end="_")
        else:
            print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


def check_uppercase_lowercase(filename):
    """Fixes 'filenames' with no space between uppercase and lowercase characters"""
    import re
    output = re.findall('[A-Z][^A-Z]*', filename)
    return output


main()
