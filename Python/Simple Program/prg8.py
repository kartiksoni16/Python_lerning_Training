# Python Program to Print the Fibonacci sequence

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233.
n = int(input())

a,b =0,1

for i in range(n):
    print(a, end="")
    a,b = b, a+b
