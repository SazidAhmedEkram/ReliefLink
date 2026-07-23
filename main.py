def main():
    while True:
        print("=============================")
        print("RELIEFLINK MAIN MENU")
        print("=============================")
        print("1. Family Management") #Easha
        print("2. Relief Inventory") # Borshon
        print("3. Shelter Management") # Sazid
        print("4. Relief Distribution") # Sazid
        print("5. Reports & Statistics") # Anurag
        print("6. Save Data")
        print("7. Exit")

        choice = input("Enter your choice: ")

        match(choice):
            case "1":
                import family_manager
                family_manager.menu()   
            case "2":
                pass
            case "3":
                # Implemented by Sazid
                import shelter_manager
                shelter_manager.menu()
            case "4":
                #Implemented by Sazid
                import relief_distribution
                relief_distribution.menu()
            case "5":
                pass
            case "6":
                pass
            case "7":
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
