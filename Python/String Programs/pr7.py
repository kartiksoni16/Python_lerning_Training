# Write a Python program to remove the characters which have odd index values of a given string.

k = "Kartik Is My Name"

result = ""
for i in range(len(k)):
    if i%2 == 0:
        result = result + k[i]

print(result)