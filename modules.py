import json
import os
from models import Family

# Load Families from JSON
def load_families():
    try:
        if os.path.exists("data/families.json"):
            with open("data/families.json", "r") as ff:
                data = json.load(ff)
            return data
        else:
            return []

    except json.JSONDecodeError:
        print("families.json contains invalid data.")
        return []

    except Exception:
        print("Error loading families.json.")
        return []


# Save Families to JSON
def save_families(data):
    try:
        if os.path.exists("data/families.json"):
            with open("data/families.json", "w") as ff:
                json.dump(data, ff, indent=4)
            return True
        else:
            print("families.json not found.")
            return False

    except Exception:
        print("Error saving families.json.")
        return False


# Validation Functions

# Check Duplicate Family ID
def validate_duplicate_id(families, familyId):

    for family in families:
        if family["familyId"] == familyId:
            return False

    return True


# Check Empty Name
def validate_name(headName):

    return headName.strip() != ""


# Check Phone Number
def validate_phone(phone):

    return phone.isdigit() and len(phone) == 11


# Check Number of Members
def validate_members(members):

    return members > 0


# Check Damage Level
def validate_damage_level(damageLevel):

    damageLevel = damageLevel.capitalize()

    if damageLevel in ["Low", "Medium", "High"]:
        return True

    return False


# Check Yes/No Input
def validate_yes_no(choice):

    choice = choice.lower()

    if choice == "yes" or choice == "no":
        return True

    return False