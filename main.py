# My Auto Country V.05
# Create a program name "CarFinder"

# Constants and initial data
DATA_FILE = "data/allowed_vehicles.txt"

SELECTION1 = "The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: "
SELECTION_EXIT = "Thank you for using the AutoCountry Vehicle Finder, good-bye!"

# Helper functions for file operations
def load_vehicles():
    try:
        with open(DATA_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return 

def save_vehicles(vehicles):
    with open(DATA_FILE, "w") as file:
        for vehicle in vehicles:
            file.write(f"{vehicle}\n")

# Core functionalities
def print_vehicles(vehicles):
    print(SELECTION1)
    for vehicle in vehicles:
        print(vehicle)

def search_vehicle(vehicles):
    search_vehicle = input("Please enter the full Vehicle name: ")
    if search_vehicle in vehicles:
        print(f"{search_vehicle} is an authorized vehicle.")
    else:
        print(f"{search_vehicle} is not an authorized vehicle. Please check the spelling and try again.")

def add_vehicle(vehicles):
    add_vehicle = input("Please Enter the full Vehicle name you would like to add: ")
    if add_vehicle not in vehicles:
        vehicles.append(add_vehicle)
        save_vehicles(vehicles)
        print(f"You have added {add_vehicle} as an authorized vehicle.")
    else:
        print(f"{add_vehicle} is already an authorized vehicle.")

def delete_vehicle(vehicles):
    delete_vehicle = input("Please Enter the full Vehicle name you would like to REMOVE: ")
    confirm_choice = input(f"Are you sure you want to remove {delete_vehicle} from the Authorized Vehicles List? (yes/no): ")
    if confirm_choice.lower() == "yes":
        if delete_vehicle in vehicles:
            vehicles.remove(delete_vehicle)
            save_vehicles(vehicles)
            print(f"You have REMOVED {delete_vehicle} as an authorized vehicle.")
        else:
            print(f"{delete_vehicle} is not in the Authorized Vehicle List.")
    elif confirm_choice.lower() == "no":
        print("Deletion cancelled.")

# Main program loop
def main():
    vehicles = load_vehicles()

    while True:
        print("********************************")
        print("AutoCountry Vehicle Finder v0.4")
        print("********************************")
        print("Please enter the following number below from the following menu:")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. ADD Authorized Vehicle")
        print("4. DELETE Authorized Vehicle")
        print("5. Exit")

        choice = input()
        if choice == "1":
            print_vehicles(vehicles)
        elif choice == "2":
            search_vehicle(vehicles)
        elif choice == "3":
            add_vehicle(vehicles)
        elif choice == "4":
            delete_vehicle(vehicles)
        elif choice == "5":
            print(SELECTION_EXIT)
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()