# https://docs.google.com/document/d/1ESVjlpDPkzOgSO3nk_ZK0VnMxoxcan7X/edit


# imple way to keep asking user for input it stops until user enters nothing.

while True:
    value = input("Enter any value : ")
    if not value:
        break
    print ("\n Your value : ",value)

# 2. Write a python program to add multiple values from user  into a list, Find out the type of a value and store that value as its type


values_list = []

while True:
    user_input = input("Enter a value (press Enter to stop): ")

    # If the user enters nothing, stop the loop
    if user_input == "":
        break

    # Try to determine the type of the value
    if user_input.isdigit():  # Check if it's an integer
        converted_value = int(user_input)
    else:
        try:
            # Attempt to convert to float
            converted_value = float(user_input)
        except ValueError:
            # If it fails, treat as string
            converted_value = user_input

    # Add the converted value to the list
    values_list.append(converted_value)

# Print the result
print("Values and their types:")
for value in values_list:
    print(f"Value: {value}, Type: {type(value)}")
# 

# 3

value_lst= []

while True:
    user = input("Enter value :")


    if user == "":
        break
    if user.isdigit():
        value_lst.append(int(user))
    else:
        print("Warning !!! Enter integer value: ")

print(value_lst)

# 4. 

list_value = []

while True:
    new_lst = input("Enter Value in it :")

    if new_lst != "":
        list_value.append(new_lst)
    else:
        break

print(list_value)

# 8
# 1

# Use list to store item name

lst_value = []

while True:
    i = input("Enter Input ")

    if i!="":
        lst_value.append(i)

    else:
        break
    

lst_value.append(20)

ls = [2,3,4,5,6,6]
ls.extend(lst_value)
print("Added one iteam in List:",lst_value)
print("Adding Multiple Iteam",ls)
ls.insert(5,200)
print("Insert item",ls)
ls.pop()
print("Remove Last Item",ls)
ls.clear()
print("Empty String")




