def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add_item = input("Add the item: ")
            return add_item
            pass
        elif choice == '2':
            remove_item = input("Enter item name: ")
            return remove_item
            # Prompt for and remove an item
            pass
        elif choice == '3':
            # Display the shopping list
            
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            return shopping_list
if __name__ == "__main__":
    main()