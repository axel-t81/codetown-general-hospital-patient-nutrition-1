# Codetown General Hospital Patient Nutrition System

## Programming Task 1 of UNE's COSC110 Introduction to Programming and the UNIX Environment

### Program Guide

This small, shell-based, Python program was an individual programming task for COSC110 at the University of New England (UNE).

While the exact requirements of the program remain the IP of UNE, the aim of the program is as following:
* Allow a hospital staff member to enter the nutrional needs of their patients.
* They do this by first entering the number of patients they are responsible for.
* They then enter the nutrional needs of each individual patient, i.e. the optimal daily protein, carbohydrates, and fat.
* Once all patient macronutrient needs have been entered, the program will:

  | Calculation | Output |
  | ----------- | ------ |
  | 1 | Average macronutrient levels across all patients (for procurement and meal planning reasons) |
  | 2 | Average kilojoules (kJs) across all patients (for medical and health reasons) |

* The program wil then close.
---

### Instructions to use the program:

1. Open shell (e.g. bash, zshell, etc)
2. Change directory (cd command) to location where tgz file was extracted.
3. (Optional) Confirm diet.py is in directory with ls command.
4. Run program via the following command
   4.1 For Python 3 machines: python3 diet.py
   4.2 For machines with earlier Python versions: python diet.py
5. (Optional) To close program prior to completion of script, simply close shell

### Instructions to access the README.md in shell:

1. Open shell (e.g. bash, zshell, etc)
2. Change directory (cd command) to location where tgz file was extracted.
3. (Optional) Confirm README.md is in directory with ls command.
4. Run and Open README.md via the following command
   4.1 For Python 3 machines: pydoc3 ./diet.py
   4.2 For machines with earlier Python versions: pydoc diet.py
