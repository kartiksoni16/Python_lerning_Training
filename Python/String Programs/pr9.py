# Write a Python program to receive a string input from user and if there are any special character such as \n or \t then program should print the entered string with new line and with a tabular space
# # 

# input = "The Sting is used to enter sequiential charcter \n Java is progaming language \n \t please use this"
# print(input)

i = input("Enter Value : ")
s = i.replace("\\n","\n").replace("\\t","\t")
print(s)