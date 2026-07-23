#Implemented By Sazid Ahmed Ekram
import json
import os
from datetime import date

# Declare the global variables
family_file = "data/families.json"
inventory_file = "data/inventory.json"
shelter_file = "data/shelters.json"
distribution_file = "data/distribution.json"

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
        match choice:
            case "1":
                family_id = input("Enter Family ID: ")
                for family in families:
                    if family_id.lower() == family["familyId"].lower():
                        found = True
                        display_family(family)
                        if check_current_status(family):
                            display_current_status(family)
                            relief_distribution(family)
                        else:
                            display_current_status(family)

            case "2":
                family_name = input("Enter Family's Head Name: ")
                for family in families:
                    if family_name.lower() == family["headName"].lower():
                        found = True
                        display_family(family)
                        if check_current_status(family):
                            display_current_status(family)
                            relief_distribution(family)
                        else:
                            display_current_status(family)

            case "3":
                phone_number = input("Enter Family's Phone Number: ")
                for family in families:
                    if phone_number == family["phone"]:
                        found = True
                        display_family(family)
                        if check_current_status(family):
                            display_current_status(family)
                            relief_distribution(family)
                        else:
                            display_current_status(family)

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
    if family["shelterNeeded"]:
        print("Shelter Needed: Yes")
    else:
        print("Shelter Needed: No")

    if family["receivedRelief"]:
        print("Received Relief: Yes")
    else:
        print("Received Relief: No")
    print("------------------------------------------------------------")


def check_current_status(family):
    return not family["receivedRelief"]

def display_current_status(family):
    if check_current_status(family):
        print("This family has already received the relief")
    else:
        print("This family is eligible for the relief")
    print("------------------------------------------------------------")

def relief_distribution(family):
    if not family["receivedRelief"]:
        package_status = ""
        if family["damageLevel"] == "High":
            print("Damage Level: High. This family will receive the Large Relief package")
            package_status = "Large"
        elif family["damageLevel"] == "Medium":
            print("Damage Level: Medium. This family will receive the Medium Relief package")
            package_status = "Medium"
        elif family["damageLevel"] == "Low":
            print("Damage Level: Low. This family will receive the Small Relief package")
            package_status = "Small"

        # Check the inventory if there is an enough stock
        if not check_inventory(package_status):
            print("Distribution failed.")
            print("Not enough stock.")
            return

        confirm = input("Distribute this package? (Y/N): ")

        if confirm.lower() != "y":
            print("Cancelled.")
            return

        update_inventory(package_status)
        update_family_status(family)
        save_distribution(package_status, family)

        print("--------------------------------")
        print("Relief Distributed Successfully")
        print("--------------------------------")


# Inventory Check
def check_inventory(package_name):
    # Load the inventory.json
    inventory = load_json(inventory_file)
    #  For Particular Package
    package = relief_package()[package_name]

    for item_name, required_qty in package.items():
        found = False
        for item in inventory:
            if item["itemName"] == item_name:
                found = True

                if item["quantity"] < required_qty:
                    print(f"Not enough {item_name}")
                    return False

        if not found:
            print(f"{item_name} not found in inventory")
            return False

    return True

def update_inventory(package_name):
    # Load
    inventory = load_json(inventory_file)
    # each package
    package = relief_package()[package_name]

    for item in inventory:
        if item["itemName"] in package:
            item["quantity"] -= package[item["itemName"]]

    save_json(inventory, inventory_file)


def update_family_status(family):
    # Load the family JSON file to the python
    families = load_json(family_file)

    for f in families:
        if f["familyId"] == family["familyId"]:
            f["receivedRelief"] = True
            break
    save_json(families, family_file)

def save_distribution(package_name, family):
    history = load_json(distribution_file)
    package = relief_package()[package_name]

    record = {
        "distributionId": f"D{len(history)+1:03}",
        "date": str(date.today()),
        "familyId": family["familyId"],
        "headName": family["headName"],
        "package": package_name,
        "items": []
    }
    inventory = load_json(inventory_file)

    for item_name, qty in package.items():
        unit = ""
        for i in inventory:
            if i["itemName"] == item_name:
                unit = i["unit"]
                break

        record["items"].append({
            "itemName": item_name,
            "quantity": qty,
            "unit": unit
        })
    history.append(record)
    save_json(history, distribution_file)

# Later I have to link this function to view the distribution history in the view features
def view_distribution_history():
    history = load_json(distribution_file)
    if len(history) == 0:
        print("No history found.")
        return

    for record in history:
        print("="*40)
        print("Distribution ID :", record["distributionId"])
        print("Date :", record["date"])
        print("Family ID :", record["familyId"])
        print("Head Name :", record["headName"])
        print("Package :", record["package"])
        print("Items")
        for item in record["items"]:
            print(f"  {item['itemName']} : {item['quantity']} {item['unit']}")
        print("="*40)

def load_json(filename):
    try:
        if os.path.isfile(filename):
            with open(filename) as f:
                return json.load(f)
        else:
            print(f"{filename} not found")
    except json.JSONDecodeError:
        return []

def save_json(data, filename):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        return True
    except json.JSONDecodeError:
        print(f"{filename} not found")
        return False

def relief_package():
    return {
        "Small": {
            "Rice": 5,
            "Water": 6,
            "Blanket": 1
        },
        "Medium": {
            "Rice": 10,
            "Water": 12,
            "Blanket": 2,
            "Medicine": 1
        },
        "Large": {
            "Rice": 20,
            "Water": 24,
            "Blanket": 5,
            "Medicine": 2,
            "Baby Food": 3,
            "Hygiene Kit": 2
        },
        "Extreme": {
            "Rice": 25,
            "Water": 24,
            "Blanket": 5,
            "Medicine": 2,
            "Baby Food": 3,
            "Hygiene Kit": 2,
            "Clothes": 1,
            "Mosquito Net": 1,
            "Cooking Oil": 1,
            "Dry Food": 5,
            "Tent": 1,
            "Torch Light": 1
        }
    }