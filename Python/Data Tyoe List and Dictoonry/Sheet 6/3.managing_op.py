my_number = 0

def display_menu():
    print("\nMenu:")
    print("1. Display My Number")
    print("2. Add into My Number")
    print("3. Subtract from My Number")
    print("4. Multiply with My Number")
    print("5. Divide My Number")
    print("6. Exit")

while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        print(f"My Number: {my_number}")
    elif choice == "2":
        value = float(input("Enter a number to add: "))
        my_number += value
        print(f"My Number after addition: {my_number}")
    elif choice == "3":
        value = float(input("Enter a number to subtract: "))
        my_number -= value
        print(f"My Number after subtraction: {my_number}")
    elif choice == "4":
        value = float(input("Enter a number to multiply: "))
        my_number *= value
        print(f"My Number after multiplication: {my_number}")
    elif choice == "5":
        value = float(input("Enter a number to divide by: "))
        if value != 0:
            my_number /= value
            print(f"My Number after division: {my_number}")
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")
