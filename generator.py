import json
import random

"""
Random Name Generator (Based from the most popular names in the year 2020)
"""
print("Random Names Generator")
print("----------------------")

with open("names.json", "r") as names:
    name = json.load(names)

with open("surnames.json", "r") as lnames:
    lname = json.load(lnames)
    lname = random.choice(lname)

gender = input("What gender do you prefer?\nM for Male and F for female.\n").lower()

if gender in ["m", "male"]:
    fname = random.choice(name["boy"])

elif gender in ["f", "female"]:
    fname = random.choice(name["girl"])

print(f"Generated Name: {fname} {lname}")