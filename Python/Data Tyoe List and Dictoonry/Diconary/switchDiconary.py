# https://docs.google.com/document/d/1p6hDJEykqQ77b-DrlqsSFIgEQ6rhyuBz/edit

# Write a python program to switch places of key value in a dictionary.

s= {"kartik" : 1, "Soni" : 2, "Badshah" : 4, 5 : "Hello"}

new = {value : key for key,value in s.items()}

s.items()


print(s)
print(new)
