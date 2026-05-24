# Write a program that asks the user for a string and a character, then removes all occurrences of that character from the string

a = input("Enter a string: ")
b = input("Enter a character to remove: ")
result = a.replace(b, "")
print("Resulting string:", result)