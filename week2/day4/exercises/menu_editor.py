from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    print("\n===== PROGRAM MENU =====")
    print("V - View an Item")
    print("A - Add an Item")
    print("D - Delete an Item")
    print("U - Update an Item")
    print("S - Show the Menu")
    print("E - Exit")
    choice = input("Choose an option: ").upper()
    if choice == 'V':
        view_item()
    elif choice == 'A':
        add_item_to_menu()
    elif choice == 'D':
        remove_item_from_menu()
    elif choice == 'U':
        update_item_from_menu()
    elif choice == 'S':
        show_restaurant_menu()
    elif choice == 'E':
        print("Exiting program. Final Menu:")
        show_restaurant_menu()
        exit()
    else:
        print("Invalid choice, try again.")

def view_item():
    name = input("Enter the name of the item to view: ")
    item = MenuManager.get_by_name(name)
    if item:
        print(f"Item found: {item.item_name} - Price: ${item.item_price}")
    else:
        print(f"Item '{name}' not found.")

def add_item_to_menu():
    name = input("Enter the item name: ")
    try:
        price = int(input("Enter the item price: "))
    except ValueError:
        print("Price must be a number.")
        return
    item = MenuItem(name, price)
    try:
        item.save()
        print(f"Item '{name}' was added successfully.")
    except Exception as e:
        print(f"Error adding item: {e}")

def remove_item_from_menu():
    name = input("Enter the name of the item to remove: ")
    item = MenuManager.get_by_name(name)
    if item:
        try:
            item.delete()
            print(f"Item '{name}' was deleted successfully.")
        except Exception as e:
            print(f"Error deleting item: {e}")
    else:
        print(f"Item '{name}' not found.")

def update_item_from_menu():
    current_name = input("Enter the current item name: ")
    item = MenuManager.get_by_name(current_name)
    if not item:
        print(f"Item '{current_name}' not found.")
        return
    try:
        current_price = int(input("Enter the current item price (for verification): "))
    except ValueError:
        print("Price must be a number.")
        return
    if current_price != item.item_price:
        print("Current price does not match the stored price. Update aborted.")
        return
    new_name = input("Enter the new item name: ")
    try:
        new_price = int(input("Enter the new item price: "))
    except ValueError:
        print("Price must be a number.")
        return
    try:
        item.update(new_name, new_price)
        print(f"Item '{current_name}' was updated successfully to '{new_name}'.")
    except Exception as e:
        print(f"Error updating item: {e}")

def show_restaurant_menu():
    print("\n===== RESTAURANT MENU =====")
    items = MenuManager.all_items()
    if not items:
        print("Menu is empty.")
    else:
        for item in items:
            print(f"{item.item_name} - ${item.item_price}")

if __name__ == "__main__":
    while True:
        show_user_menu()
