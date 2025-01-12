# Write a Python program to swap cases of a given string.

# k = "Badshah Is my name"
# l = "My name is Kartik"
# m = ""

# m=k
# k=l
# l=m

# print(k)
# print(l)

k = "Kartik iS GooD Boy"
result = ""

for i in k:
    if i.islower():
        result = result + i.upper()
    else:
        result = result + i.lower()

print(result)

# Using function # type: ignore

def swap_char(s):
    result = ""

    for j in s:
        if j.islower():
            result = result + j.upper()
        else:
            result = result + j.lower()

    return result

print(swap_char("My NAme is Kartik"))
