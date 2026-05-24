# Write a program to check if a string contains any digits.

a = input("Enter a string: ")
for char in a: 
    if char.isdigit():
        print("The string contains digits.")
        break
else:    
    print("The string does not contain any digits.")