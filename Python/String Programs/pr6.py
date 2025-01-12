# Write a Python program to remove unwanted characters from a given string.


s = "Geeks, forGeeks! 123."
cleaned = ''.join(char for char in s if char.isalnum())
print(cleaned)


s = "Geeks,forGeeks! 123."
cleaned = ''.join(filter(str.isalnum, s))
print(cleaned)