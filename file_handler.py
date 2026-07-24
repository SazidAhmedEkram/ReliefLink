# Implemented by Anurag Sarkar
# JSON File Handling
# Exception Handling
# Data Persistence

import json

# File Paths
FAMILY_FILE = "data/families.json"
INVENTORY_FILE = "data/inventory.json"
SHELTER_FILE = "data/shelters.json"
DISTRIBUTION_FILE = "data/distribution.json"


# -----------------------------
# Load Data From JSON File
# -----------------------------
def load_json(filename):

    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return []

    except json.JSONDecodeError:
        print(f"Error: The file '{filename}' contains invalid data.")
        return []

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


# -----------------------------
# Save Data To JSON File
# -----------------------------
def save_json(data, filename):

    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        return True

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


# -----------------------------
# Family File
# -----------------------------
def load_families():
    return load_json(FAMILY_FILE)


def save_families(families):
    return save_json(families, FAMILY_FILE)


# -----------------------------
# Inventory File
# -----------------------------
def load_inventory():
    return load_json(INVENTORY_FILE)


def save_inventory(inventory):
    return save_json(inventory, INVENTORY_FILE)


# -----------------------------
# Shelter File
# -----------------------------
def load_shelters():
    return load_json(SHELTER_FILE)


def save_shelters(shelters):
    return save_json(shelters, SHELTER_FILE)


# -----------------------------
# Distribution File
# -----------------------------
def load_distribution():
    return load_json(DISTRIBUTION_FILE)


def save_distribution(distribution):
    return save_json(distribution, DISTRIBUTION_FILE)