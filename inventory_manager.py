#Implementation-Borshon Debnath

import json
inventory_file = "data/inventory.json"

def inventoryMenu():
    while True:
        print("Inventory Management")
        print("1.Add Item")
        print("2.View Items")
        print("3.Search Item")
        print("4.Update Quantity")
        print("5.Delete Item")
        print("6.Low Stock Alert")
        print("7.Back")

        option=input("Enter your option")

        if option == "1":
            print("Add Item Selected")
        elif option == "2":
            viewItems()   
        elif option == "3":
            print("Search Item Selected")
        elif option == "4":
            print("Update Quantity Selected")            
        elif option == "5":
            print("Delete Item Selected")    
        elif option == "6":
            print("Low Stock Alert Selected")  
        elif option == "7":
            print("Returning to main menu")

        else:
            print("Invalid Option")                                             

def viewItems():
    try:
        with open(inventory_file,"r") as file:
            items=json.load(file)

        print("-----INVENTORY----")

        for item in items:
            print(f"Item ID:{item['itemId']}")
            print(f"Name:{item['itemName']}")
            print(f"Quantity:{item['quantity']} {item['unit']}")
            print(f"Minimum:{item['minimumStock']}")
            print("----------------------------")

    except FileNotFoundError:
        print("Inventory file not found.")


if __name__ == "__main__":
    inventoryMenu()        