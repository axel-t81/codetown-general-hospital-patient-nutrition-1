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

justify = " "
line = "*"

# A function to collect valid input for macro nutritional data
# This function validates input to confirm (a) it is a number that fits the requirements of a float, and (b) that it is non-negative.
# For citing sources, this function is from learning from StackOverflow
# My original StackOverflow question was asked here: https://stackoverflow.com/questions/78814504/in-python-why-is-this-negative-float-passing-the-non-negative-while-loop-test-c
# And not only did @Andrew Yim answer my original question, he pointed me to a StackFlow guide on how to better tackle this input validation problem.
# The guide he pointed me to was here: https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
# For learning quickly about Try and Except, this guide was used: https://www.youtube.com/watch?v=MImAiZIzzd4
def non_negative_only(prompt):
    while True:
        try:
            value = float(input(prompt))
        except:
            print("Sorry, I didn't understand your input. Let's try again, using a whole number or one with decimal places, as your input please.")
            continue

        if value < 0:
            print("Sorry, the amount must be a non-negative number. Please try again.")
            continue
        else:
            break
    return value

# A function to collect valid input for patients numbers
# This function validates input to confirm (a) it is an integer to count people, and (b) that it is positive and above zero.
def positive_int_only(prompt):
    while True:
        try:
            value = int(input(prompt))
        except:
            print("Sorry, I didn't understand your input. Let's try again, using a whole number to count people, as your input please.")
            continue

        if value < 1:
            print("Sorry, the number of patients must be a positive number. Please try again.")
            continue
        else:
            break
    return value

def right_align(input_string):
    info = input_string
    characters = len(info)
    blanks = 10 - characters
    return (blanks*justify + info)

# value = input("Enter string to justify: ")
# right_justify(value)

# Guarded main function, as per https://www.python-boilerplate.com/py3+executable
# A guarded main function prevents the program being run when it is imported elsewhere?
def main():
    # For UI and user-friendliness, provide feedback to user of program start/entry point.
    print("\n" + line*100)
    print("WELCOME TO THE CODETOWN GENERAL HOSPITAL PATIENT NUTRITION SYSTEM:")
    print(line*100 + "\n")
    # Requirement 1: "request the number of patient's dietary requirements that will be entered in the interaction with the program"
    patients = positive_int_only("\nHow many patients are you collecting data for, today? ")


    # For UI and user-friendliness, provide feedback and guidance to user of where they are in the program.
    print("\n\nSTEP 1 of 2 - PATIENT NUTRITION COLLECTION:")
    # Requirement 2: "loop this number of times to collect the amount of protein, carbohydrates, and fat required for each patient."
    # Using range() allows the fort loop to be interable over an int
    for x in range(patients):
        # For UI and user-friendliness, when describing patient to user, add 1 to zero-based index and typecast int x to string
        x_string = str(x + 1)

        protein = non_negative_only("\nHow many grams of protein is required for patient " + x_string + "? ")
        # Append most recent entry to end of appropriate List.
        all_protein.append(protein)

        carbs = non_negative_only("\nHow many grams of carbohydrates are required for patient " + x_string + "? ")
        all_carbs.append(carbs)

        fat = non_negative_only("\nHow many grams of fat is required for patient " + x_string + "? ")
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
    print("\n\nSTEP 2 of 2 - CALCULATED PATIENT INFORMATION:\n")
    protein_average_float = round(sum(all_protein) / len(all_protein),2)
    protein_average = right_align(str(f'{protein_average_float:.2f}'))
    print("Protein - The average protein for all patients is:" + justify*13 + protein_average + " grams")

    carbs_average_float = round(sum(all_carbs) / len(all_carbs),2)
    carbs_average = right_align(str(f'{carbs_average_float:.2f}'))
    print("Carbohydrates - The average carbohydrates for all patients is:" + justify*1 + carbs_average + " grams")

    fat_average_float = round(sum(all_fat) / len(all_fat),2)
    fat_average = right_align(str(f'{fat_average_float:.2f}'))
    print("Fat - The average fat for all patients is:" + justify*21 + fat_average + " grams")

    kjs_average_float = round(sum(all_kjs) / len(all_kjs),2)
    kjs_average = right_align(str(f'{kjs_average_float:.2f}'))
    print("Kilojoules - The average kilojoules for all patients is:" + justify*7 + kjs_average + " kJs\n")

    print("\n" + line*100)
    print("THE SYSTEM IS NOW COMPLETE: YOUR PATIENTS' NUTRITIONAL INFORMATION IS NOW AVAILABLE FOR USE.\nPLEASE CLOSE THIS PROGRAM OR RUN AGAIN. THANK YOU.")
    print(line*100 + "\n")

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()



