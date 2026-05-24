# Write a program that accepts a username and password and checks if both are not empty
username = input("Enter your username: ")
password = input("Enter your password: ")
print("Username and password are not empty:", bool(username) and bool(password))