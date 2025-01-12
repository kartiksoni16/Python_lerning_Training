# Python Program to Find the Largest Among Three Numbers


n = int(input("Enter Number of 1 : "))
m = int(input("Enter Number of 2 : "))
l = int(input("Enter Number of 3 : "))


# Using Max Function
max = max(n,m,l)
print(f"Largest number is {max}")


# Using if condition
if n > m and n > l:
    print("N is largest Number")
elif m > n and n > l:
    print("M is largest Number")
else:
    print("L is largest")