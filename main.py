#!/usr/bin/env python3
"""
Module Docstring
"""

# Program Details to Provide, as per https://www.python-boilerplate.com/py3+executable
__author__ = "Axel Tracy"
__version__ = "0.1.0"
__license__ = "None. All Rights Reserved."

# Initialise empty Lists for each macro.
# Use Lists as they allow duplicates, are changeable, and can be looped through and worked on
all_protein = []
all_carbs = []
all_fat = []
all_kjs = []

# Guarded main function, as per https://www.python-boilerplate.com/py3+executable
# A guarded main function prevents the program being run when it is imported elsewhere?
def main():
    # Requirement 1: "request the number of patient's dietary requirements that will be entered in the interaction with the program"
    print("How many patients are you collecting data for, today?")
    patients_string = input()
    # input() collects values as strings, so typecast to int
    patients = int(patients_string)

    # Requirement 2: "loop this number of times to collect the amount of protein, carbohydrates, and fat required for each patient."
    # Using range() allows the fort loop to be interable over an int
    for x in range(patients):
        # For UI and user-friendliness, add 1 to zero-based index and typecast int x to string
        x_string = str(x + 1)

        print("How much protein is required for patient " + x_string + "?")
        protein_string = input()
        protein = int(protein_string)
        # Append most recent entry to end of appropriate List
        all_protein.append(protein)

        print("How many carbohydrates are required for patient " + x_string + "?")
        carbs_string = input()
        carbs = int(carbs_string)
        all_carbs.append(carbs)

        print("How much fat is required for patient " + x_string + "?")
        fat_string = input()
        fat = int(fat_string)
        all_fat.append(fat)

        # Print functions for testing and understanding by programmer
        print(all_protein)
        print(all_carbs)
        print(all_fat)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()