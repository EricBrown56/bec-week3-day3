#Problem Statement:  Write a function that takes in a list of names, and verifies that the names are valid names using a regex pattern and match(), and prints the name if it is valid, "Invalid name" if the name is not.

import re

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]

def validate_names(names):
    for name in names:
        if re.match(r'[A-Z][a-z]+ |\w [A-Z][a-z]+', name): # [A-Z][a-z]+: first name, [A-Z][a-z]+: last name, we put the or function to optionally match the middle name if there was one
            print(name)
        else:
            print("Invalid name")

validate_names(names)