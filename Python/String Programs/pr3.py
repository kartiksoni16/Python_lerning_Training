# Write a Python program to find the smallest and largest word in a given string

k = "Kartik is my name but prgramming is my hobby"

m = k.split(" ")

smallest = m[0]
largest = m[0]
    

for m1 in m:
    if len(m1) < len(smallest):
        smallest = m1
    elif len(m1) > len(largest):
        largest = m1

print(smallest)
print(largest)

