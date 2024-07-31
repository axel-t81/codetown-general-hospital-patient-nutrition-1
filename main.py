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
    # Using the float() function avoids the 'Value Error' when their is an 'invalid literal' entered in the input, eg a decimal
    patients = int(float(patients_string))

    while patients < 1:
        print("Sorry, the number of patients must be a positive number. Please try again.")
        print("How many patients are you collecting data for, today?")
        patients_string = input()
        patients = int(float(patients_string))

    # Requirement 2: "loop this number of times to collect the amount of protein, carbohydrates, and fat required for each patient."
    # Using range() allows the fort loop to be interable over an int
    for x in range(patients):
        # For UI and user-friendliness, add 1 to zero-based index and typecast int x to string
        x_string = str(x + 1)

        print("How many grams of protein is required for patient " + x_string + "?")
        protein_string = input()
        protein = float(protein_string)
        while protein < 0.0:
            print("Sorry, the amount must be a non-negative number. Please try again.")
            print("How many grams of protein is required for patient " + x_string + "?")
            protein_string = input()
            protein = float(protein_string)
        # Append most recent entry to end of appropriate List
        all_protein.append(int(protein))

        print("How many grams of carbohydrates are required for patient " + x_string + "?")
        carbs_string = input()
        carbs = int(float(carbs_string))
        while carbs < 0.0:
            print("Sorry, the amount must be a non-negative number. Please try again.")
            print("How many grams of carbohydrates are required for patient " + x_string + "?")
            carbs_string = input()
            carbs = int(float(carbs_string))
        all_carbs.append(carbs)

        print("How many grams of fat is required for patient " + x_string + "?")
        fat_string = input()
        fat = int(float(fat_string))
        while fat < 0:
            print("Sorry, the amount must be a non-negative number. Please try again.")
            print("How many grams of fat are required for patient " + x_string + "?")
            fat_string = input()
            fat = int(float(fat_string))
        all_fat.append(fat)

        # Calculate Kjs for each patient, and add it to the appropriate List
        kilojoules_unrounded = (4.18 * (4 * protein + 4 * carbs + 9.30 * fat))
        kilojoules = round(kilojoules_unrounded, 4)
        all_kjs.append(kilojoules)

    ## Print functions for testing and understanding by programmer
    ## print(all_protein)
    ## print(all_carbs)
    ## print(all_fat)
    ## print(all_kjs)

    # Calculate and Output Averages of All Four Lists
    protein_average_float = round(sum(all_protein) / len(all_protein),2)
    protein_average = str(protein_average_float)
    print("The average protein for all patients is " + protein_average + " grams.")

    carbs_average_float = round(sum(all_carbs) / len(all_carbs),2)
    carbs_average = str(carbs_average_float)
    print("The average carbohydrates for all patients is " + carbs_average + " grams.")

    fat_average_float = round(sum(all_fat) / len(all_fat),2)
    fat_average = str(fat_average_float)
    print("The average fat for all patients is " + fat_average + " grams.")

    kjs_average_float = round(sum(all_kjs) / len(all_kjs),2)
    kjs_average = str(kjs_average_float)
    print("The average kilojoules for all patients is " + kjs_average + " kJs.")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()