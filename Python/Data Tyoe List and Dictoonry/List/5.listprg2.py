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

    if user_input == "":
        break
    
    if user_input.isdigit():  
        converted_value = int(user_input)
    elif user_input.isalpha():
        converted_value = user_input
    else:
        converted_value = float(user_input)    

    values_list.append(converted_value)

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

# 4. Manage a shopping list with python list,

list_value = []

while True:
    new_lst = input("Enter Value in it :")

    if new_lst != "":
        list_value.append(new_lst)
    else:
        break

print(list_value)


# Manage two lists to store an integer values.

first=[]
second=[]

while True:
    user_new = input("Enter number from the user")

    if user_new == "":
        break

    user_new = int(user_new)

    if user_new % 2 == 0:
        first.append(user_new)
    else:
        second.append(user_new)

print("Even Number",first)
print("Odd Number",second)

print("Maximum No from",max(first))


# Manage two lists, so that you can manage customer name and customer shopping list

cs_name = []
cs_shop_list= []

while True:
    
    cs_n = input("Enter Customer Name : ").strip()

    if not cs_n:
        break

    cs_name.append(cs_n)


    shopping_list = []
    print(f"Enter shopping items for {cs_name} (type nothing and press Enter to finish):")

    while True:

        cs_list = input("Enter Customer Shopping list").strip()

        if not cs_list:
            break

        shopping_list.append(cs_list)

    cs_shop_list.append(shopping_list)


for customer,item in zip(cs_name,cs_shop_list):
    print(f"{customer} : {item}")



# Wite a python program to enter multiple values into a two lists and merge them but remove duplication of value only appear one time.


# lst_1 =[]
# lst_2=[]

# def merge_list(v):

#     l = input("Enter first value").strip()

#     while True:

#         if not l:
#             break

#         lst_2.append(l)

# lst_1 = merge_list("List 1")
# lst_2 = merge_list("List 2")

# merge = list(set(lst_1 + lst_2))

# print(merge)

# Define global variables
lst_1 = []
lst_2 = []

def merge_list(prompt):
    global lst_1, lst_2  # Declare that we're using the global variables
    print(f"Enter values for {prompt} (type nothing and press Enter to stop):")
    while True:
        value = input("Enter value: ").strip()
        if not value:  # Stop when input is empty
            break
        if prompt == "List 1":
            lst_1.append(value)  # Modify global variable lst_1
        elif prompt == "List 2":
            lst_2.append(value)  # Modify global variable lst_2

# Use the function to populate the lists
merge_list("List 1")
merge_list("List 2")

# Merge and remove duplicates
merge = list(set(lst_1 + lst_2))

# Print the merged list
print("Merged List with Unique Values:", merge)


# Write a python program to manage shopping list.

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




