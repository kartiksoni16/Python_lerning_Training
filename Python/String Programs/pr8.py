# Write a Python program to receive a string from the user and ask the user to add after which characters he/she wants to add a new line character.

a = "My name is kartik and my work is to build and develop code."

print("Without New line", a)
g = "My name is kartik \n and my work is to \n build and develop code."

print("Added New line", g)


# Get input from the user
input_string = input("Enter the string: ")
characters_to_add_newline = input("Enter the characters after which to add a newline (e.g., '.!?'): ")

# Process the string
for char in characters_to_add_newline:
    input_string = input_string.replace(char, char + "\n")

print(input_string)
