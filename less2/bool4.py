# Write a program that takes three numbers and checks if all of them are different
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
print("All numbers are different:", a != b and b != c and a != c)