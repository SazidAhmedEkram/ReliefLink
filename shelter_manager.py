# Implemented by Sazid Ahmed Ekram
import json
import main
from unittest import case


# This is the menu linked to the main.py
def menu():
    while True:
        print("=============================")
        print("Choose a option please")
        print("=============================")
        print("1. Add Shelter")
        print("2. View Shelter")
        print("3. Search Shelter")
        print("4. Update Shelter")
        print("5. Delete Shelter")
        print("6. Allocate Family")
        print("7. Remove Family")
        print("8. Go Back")

        choose = input("Enter your choice: ")
        match(choose):
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                pass
            case "8":
                return
            case _:
                print("Invalid choice. Please try again.")




# Load the data from the JSON
def load_shelters():
    with open('shelters.json', "r") as sf:
        return json.load(sf)

# Save the data to the JSON
def save_shelters(data):
    with open('shelters.json', "w") as sf:
        json.dump(data, sf, indent=4)

