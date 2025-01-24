# https://docs.google.com/document/d/127v-skq2pCmpu5kN768WZ9jqnR6Knm3f/edit


# with tabular 
import tabulate

def get_employee_details():
    
    employee = {}
    employee['name'] = input("Enter employee's name: ")
    employee['mobile'] = input("Enter employee's mobile number: ")
    employee['email'] = input("Enter employee's email address: ")
    employee['birthdate'] = input("Enter employee's birthdate (YYYY-MM-DD): ")
    employee['position'] = input("Enter employee's position: ")
    employee['city'] = input("Enter employee's city: ")
    return employee

def display_employees(employee_list):
    
    if not employee_list:
        print("No employees to display.")
        return

    headers = ['Name', 'Mobile', 'Email', 'Birthdate', 'Position', 'City']
    rows = [
        [employee['name'], employee['mobile'], employee['email'], employee['birthdate'], employee['position'], employee['city']] 
        for employee in employee_list
    ]

    print("\nEmployee Details:")
    print(tabulate.tabulate(rows, headers=headers, tablefmt="grid"))

def main():

    employee_list = []  

    while True:
        print("\n--- Employee Management System ---")
        print("1. Add a new employee")
        print("2. Display all employees")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            employee = get_employee_details()
            employee_list.append(employee)
            print("Employee added successfully!")

        elif choice == '2':
            display_employees(employee_list)

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()

