# Implemented by Sazid Ahmed Ekram
import json
import os
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
                add_shelter()
            case "2":
                viw_shelter()
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
# Convert the Json to Python's Dictionary
def load_shelters():
    try:
        if os.path.exists("data/shelters.json"):
            with open('data/shelters.json', "r") as sf:
                return json.load(sf)
        else:
            print("Shelters.json not found")
    except json.JSONDecodeError:
        return []
# Save the data to the JSON
def save_shelters(data):
    try:
        if os.path.exists("data/shelters.json"):
            with open('data/shelters.json', "w") as sf:
                json.dump(data, sf, indent=4)
            return True
    except json.JSONDecodeError:
        print("Shelters.json not found")
        return False


def add_shelter():
    shelters = load_shelters() # shelters is a list of dictionary
    shelter_id = int(input("Enter Shelter ID: "))
    name = input("Enter Shelter Name: ")
    district = input("Enter Shelter District: ")
    capacity = int(input("Enter Shelter Capacity: "))

    # Check the dublicate data
    for shelter in shelters:
        if shelter["shelterId"] == shelter_id:
            print("Shelter Id Already Exists")
            return
    # Import the ShelterManagement Class from shelter_manager module
    from shelter_management import ShelterManagement
    new_shelter = ShelterManagement(
        shelterId=shelter_id,
        shelterName=name,
        district=district,
        capacity=capacity,
    )
    # Convert to the Json file
    shelter_data = new_shelter.to_shelter_json()
    shelters.append(shelter_data)

    if save_shelters(shelters):
        print("Shelters Saved")
    else:
        print("Shelters Not Saved")


def viw_shelter():
    shelters = load_shelters()
    if len(shelters) == 0:
        print("Shelters Not Found")
        return
    for shelter in shelters:
        print("=============================")
        print(f"Shelter Id: {shelter["shelterId"]}")
        print(f"Shelter Name: {shelter["shelterName"]}")
        print(f"Shelter District: {shelter["district"]}")
        print(f"Shelter Capacity: {shelter["capacity"]}")
        print(f"Current Occupancy: {shelter['currentOccupancy']}")
        print("=============================")