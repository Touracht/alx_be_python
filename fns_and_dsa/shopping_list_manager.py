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

        if choice == '1' :
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"{shopping_list} has been added to the list.")
            # Prompt for and add an item
            pass
        elif choice == '2' :
            item = input("Enter the item you want to remove: ")
            if item in shopping_list:
               shopping_list.remove(item)
               print(f"{shopping_list} has been removed from the list.")
            # Prompt for and remove an item
            pass
        elif choice == '3' :
            if shopping_list:
                for item in shopping_list:
                    print(item)
            # Display the shopping list
            pass
        elif choice == '4' :
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()