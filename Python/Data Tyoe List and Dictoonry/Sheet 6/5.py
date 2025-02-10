from tabulate import tabulate

def add_item(shopping_list, item):
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to the shopping list.")
    else:
        print("Item cannot be empty!")

def add_multiple_items(shopping_list, items):
    items_list = items.split(',')
    items_list = [item.strip() for item in items_list if item.strip()]
    if items_list:
        shopping_list.extend(items_list)
        print(f"Items {items_list} have been added to the shopping list.")
    else:
        print("No valid items to add!")

def add_item_at_index(shopping_list, index, item):
    try:
        index = int(index)
        if item:
            shopping_list.insert(index, item)
            print(f"'{item}' has been added at index {index}.")
        else:
            print("Item cannot be empty!")
    except ValueError:
        print("Index must be a valid integer!")

def remove_last_item(shopping_list):
    if shopping_list:
        removed_item = shopping_list.pop()
        print(f"'{removed_item}' has been removed from the shopping list.")
    else:
        print("Shopping list is already empty!")

def remove_item_by_name(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the shopping list.")
    else:
        print(f"'{item}' not found in the shopping list!")

def empty_list(shopping_list):
    shopping_list.clear()
    print("Shopping list has been emptied.")

def replace_item(shopping_list, old_item, new_item):
    if old_item in shopping_list:
        index = shopping_list.index(old_item)
        shopping_list[index] = new_item
        print(f"'{old_item}' has been replaced with '{new_item}'.")
    else:
        print(f"'{old_item}' not found in the shopping list!")

def display_list(shopping_list):
    if shopping_list:
        table = [[index, item] for index, item in enumerate(shopping_list)]
        print(tabulate(table, headers=["Index", "Item"], tablefmt="grid"))
    else:
        print("Shopping list is empty!")

def main():
    shopping_list = []
    while True:
        print("\nMenu:")
        print("1. Add an item")
        print("2. Add multiple items")
        print("3. Add an item at index")
        print("4. Remove last added item")
        print("5. Remove an item with name")
        print("6. Remove all items/Empty list")
        print("7. Replace an item with new item")
        print("8. Display list")
        print("(Press Enter without input to exit)")

        choice = input("Enter your choice: ")
        if not choice:
            print("Exiting program. Goodbye!")
            break

        if choice == "1":
            item = input("Enter the item to add: ")
            add_item(shopping_list, item)
        elif choice == "2":
            items = input("Enter items separated by commas: ")
            add_multiple_items(shopping_list, items)
        elif choice == "3":
            index = input("Enter the index to add at: ")
            item = input("Enter the item to add: ")
            add_item_at_index(shopping_list, index, item)
        elif choice == "4":
            remove_last_item(shopping_list)
        elif choice == "5":
            item = input("Enter the item to remove: ")
            remove_item_by_name(shopping_list, item)
        elif choice == "6":
            empty_list(shopping_list)
        elif choice == "7":
            old_item = input("Enter the item to replace: ")
            new_item = input("Enter the new item: ")
            replace_item(shopping_list, old_item, new_item)
        elif choice == "8":
            display_list(shopping_list)
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()
