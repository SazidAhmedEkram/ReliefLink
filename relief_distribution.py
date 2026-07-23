#Implemented By Sazid Ahmed Ekram
import json
import os
from unittest import case

# Declare the global variables
family_file = "data/families.json"
inventory_file = "inventory.json"
shelter_file = "shelter.json"

def menu():
    while True:
        print("=============================")
        print("Relief-Distribution")
        print("===========================")
        print("You need to search a Family to distribute the relief")
        print("1. Search Family By ID")
        print("2. Search Family By Name")
        print("3. Search Inventory By Phone Number")
        print("4. Go Back")

        choice = input("Enter your choice: ")
        families = load_json(family_file)
        found = False
        match(choice):
            case "1":
                family_id = input("Enter Family ID: ")
                for family in families:
                    if family_id.lower() == family["familyId"].lower():
                        found = True
                        display_family(family)
                        display_current_satus(family)

            case "2":
                family_name = input("Enter Family's Head Name: ")
                for family in families:
                    if family_name.lower() == family["headName"].lower():
                        found = True
                        display_family(family)
                        display_current_satus(family)
            case "3":
                phone_number = input("Enter Family's Phone Number: ")
                for family in families:
                    if phone_number == family["phone"]:
                        found = True
                        display_family(family)
                        display_current_satus(family)
            case "4":
                return
            case _:
                print("Invalid choice")

        if not found:
            print("There is no family with that information")

def display_family(family):
    print("------------------------------------------------------------")
    print("Family ID: ", family["familyId"])
    print("Family Head's Name: ", family["headName"])
    print("Phone Number: ", family["phone"])
    print("District: ", family["district"])
    print("upazila", family["upazila"])
    print("village: ", family["village"])
    print("Family Members: ", family["members"])
    print("Children: ", family["children"])
    print("Elderly: ", family["elderly"])
    print("Disabled Members: ", family["disabledMembers"])
    print("Damage Level: ", family["damageLevel"])
    if family["shelterNeeded"] == True:
        print("Shelter Needed: Yes")
    else:
        print("Shelter Needed: No")

    if family["receivedRelief"] == True:
        print("Received Relief: Yes")
    else:
        print("Received Relief: No")
    print("------------------------------------------------------------")


def display_current_satus(family):
    if family["receivedRelief"] == True:
        print("This family has already received the relief")
    else:
        print("This family is eligible for the relief")
    print("------------------------------------------------------------")

def relief_distribution():
    pass

def load_json(filename):
    try:
        if os.path.isfile(filename):
            with open(filename) as f:
                return json.load(f)
        else:
            print("Families.json not found")
    except json.JSONDecodeError:
        return []

def save_json(data, filename):
    try:
        if os.path.isfile(filename):
            with open(filename, "w") as f:
                json.dump(data, f, indent=4)
            return True
    except json.JSONDecodeError:
        print("Families.json not found")
        return False