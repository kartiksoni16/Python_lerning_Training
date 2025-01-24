
# https://docs.google.com/document/d/1SIWexX4B37ItGCMFSGbVXsnH2QaPMqOb/edit?usp=sharing&ouid=102243004211544304598&rtpof=true&sd=true
# Find out multiple ways of determining variable data type like integer, string or list.
#

k = [1,2,3,"Kartik",{1,2,3,4}]
# k = ["1","2","3","Kartik"]
print(k)
print(type(k))

for i in k:
    print(i)

# # # 1. Write a Python program to sum all the items in a list.

input = input("Enter List Iteam").split()
print(input)
s = 0
for i in input:
    s = s + int(i)
 
print(s)

# 3. 2. Write a Python program to multiply all the items in a list.

l = [2,3,4,5,6,7]
k=1
for i in l:
    k = k * int(i)
    # print(f"{k} * {i}")
    print(k)

print(k)

# 3. Write a python program to find the second maximum number from a list of numbers.

n = [1,2,5,6,8,5,6]

s = set(n)
print(s)

f = list(s)
print(f)
print(f[-2])

print(f)

# 4. Write a python program to add integer values into a list.
#     Add value at the beginning of the list if the value is odd.
#     Add value at the end of the list if the value is even.

def find_odd_even(value,list):
    if value%2 == 0:
        list.append(value)
    else:
        list.insert(0,value)

l = []
values=[2,3,4,5,3,2,4]

for value in values:
    find_odd_even(value,l)
 
print(l)

# 5.

def find_count_value(lt):
    result=[]
    unique = set(lt)
    # print(unique)
    for value in unique:
        count = lt.count(value)
        result.append((value,count))
    return sorted(result)
    


lt = [1,2,3,3,2,1,5,6,7,7,7,8,9,0,1,2,0]
result = find_count_value(lt)
print(result)


# 6. Write a python program to filter out the list of numbers that are odd and even
#     - lst = [1,2,3,4,5,6,7,8,9]
#     Result :
#     - odd_numbers = [1,3,5,7,9]
#     - even_numbers = [2,4,6,8]

list = [1,2,3,4,5,6,7,8,9]

odd_number = []
even_number = []

for i in list:
    if i%2==0:
        even_number.append(i)
    else:
        odd_number.append(i)

print("Even Number", even_number)
print("Odd Number", odd_number)

# Using List Compression    
odd_number = [i for i in list if i%2 == 0]
even_number = [i for i in list if i%2 != 0]

print(odd_number)
print(even_number)


# 7. Write a python program to determine if the switch is on or off,
    # - use the given truth table for checking values and showing results.


switch_1 = int(input("Enter Numer: "))
switch_2 = int(input("Enter Numer: "))

if switch_1  == 1:
    if switch_2 == 1:
        print ("1")
    else:
        print("0")
else:
    print("Number is not right It should be under 1 and 0")