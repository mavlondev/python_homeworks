# boolean

# Write a program that accepts a username and password and checks if both are not empty
username = input("Enter your username: ")
password = input("Enter your password: ")
print("Username and password are not empty:", bool(username) and bool(password))

# Create a program that checks if two numbers are equal and outputs a message if they are.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("The numbers are equal." if a == b else "The numbers are not equal.")

# Write a program that checks if a number is positive and even
a = int(input("Enter a number: "))
print(a > 0 and a % 2 == 0)

# Write a program that takes three numbers and checks if all of them are different
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
print("All numbers are different:", a != b and b != c and a != c)

# Create a program that accepts two strings and checks if they have the same length
a = input("Enter the first string: ")
b = input("Enter the second string: ")
print("The strings have the same length:", len(a) == len(b))

# Create a program that accepts a number and checks if it’s divisible by both 3 and 5.
a = int(input("Enter a number: "))
print(a % 3 == 0 and a % 5 == 0)

# Write a program that checks if the sum of two numbers is greater than 50.8
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("The sum of the two numbers is greater than 50.8:", (num1 + num2) > 50.8)

# Create a program that checks if a given number is between 10 and 20 (inclusive)
a = int(input("Enter a number: "))
print(a >= 10 and a <= 20)

# -------------------------------------------

# number

# Create a program that takes a float number as input and rounds it to 2 decimal places
number = float(input('Enter a float number: '))
print(f"{number:.2f}")

# Write a Python file that asks for three numbers and outputs the largest and smallest.

a, b, c = map(int, input().split())
print(f" Largest: {max(a, b, c)}")
print(f" Smallest: {min(a, b, c)}")

# Create a program that converts kilometers to meters and centimeters.
 
km = float(input('Enter distance in kilometers: '))
meters = km * 1000
centimeters = km * 100000
print(f"Distance in meters: {meters}")
print(f"Distance in centimeters: {centimeters}")

# Write a program that takes two numbers and prints out the result of integer division and theremainder.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(divmod(a, b))

# Make a program that converts a given Celsius temperature to Fahrenheit
c = float(input("Enter the temperature in Celsius: "))
f = (c * 9/5) + 32
print(f"{c} degrees Celsius is equal to {f} degrees Fahrenheit")

# Create a program that accepts a number and returns the last digit of that number.
a = int(input("Enter a number: "))
print(f"The last digit of the number is: {a%10}")

# Create a program that takes a number and checks if it’s even or not
a = int(input("Enter a number: "))
print(["Odd", "Even"][a % 2 == 0])

# -------------------------------------------
# string

# Create a program to ask name and year of birth from user and tell them their age
name = input("What is your name? ")
year = int(input("When were you born? "))
age = 2026-year
print(f"Hello, {name}! Your age is {age}.")

# Extract car names from this text: txt = 'LMaasleitbtui'
txt = 'LMaasleitbtui'
first_word = txt[0::2]
second_word = txt[1::2]
print(first_word, second_word)

"""
Write a Python program to:

    Take a string input from the user.
    Print the length of the string.
    Convert the string to uppercase and lowercase.
"""

a = input("Enter a string: ")
print("Length of the string:", len(a))
print(a.upper())
print(a.lower())

# Write a Python program to check if a given string is palindrome or not.

a = input("Enter a palindrome string: ")
print(a == a[::-1])

# Write a program that counts the number of vowels and consonants in a given string
a = input("Enter a string: ")
vowels = "aeiou"
vowel_count = 0
for char in a.lower():
    if char in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count) 
print("Number of consonants:", len(a) - vowel_count)

# Write a Python program to check if one string contains another
a = input("Enter a string: ")
b = input("Enter a string: ")

print((a in b) | (b in a))

"""
Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.
Example:

    Input sentence: "I love apples."
    Replace: "apples"
    With: "oranges"
    Output: "I love oranges."
"""

s = input("Input sentence: ")
r = input("Replace: ")
word = input("With: ")
print(s.replace(r, word))

# Write a program that asks the user for a string and prints the first and last characters of the string.

a = input("Enter a string: ")
print("First character:", a[0])
print("Last character:", a[-1])

# Ask the user for a string and print the reversed version of it.
a = input("Enter a string: ")
print("Reversed string:", a[::-1])

# Write a program that asks the user for a sentence and prints the number of words in it.
a = input("Enter a sentence: ")
print(len(a.split()))

# Write a program to check if a string contains any digits.

a = input("Enter a string: ")
for char in a: 
    if char.isdigit():
        print("The string contains digits.")
        break
else:    
    print("The string does not contain any digits.")

# Write a program that takes a list of words and joins them into a single string, separated by a character (e.g., - or ,).
a = input("Enter a string in one line with spaces: ")
print("-".join(a.split()))

# Ask the user for a string and remove all spaces from it
a = input("Enter a string: ")
a = a.replace(" ", "")
print("String without spaces:", a)

# Write a program to ask for two strings and check if they are equal or not
a = input("Enter the first string: ")
b = input("Enter the second string: ") 
print("The strings are equal: ", a == b)

"""
Ask the user for a sentence and create an acronym from the first letters of each word.
Example:

    Input: "World Health Organization"
    Output: "WHO"

"""
sentence = input("Enter a sentence: ")
acronym = ""
for word in sentence.split():
    acronym += word[0].upper()
print("Acronym:", acronym)

# Write a program that asks the user for a string and a character, then removes all occurrences of that character from the string

a = input("Enter a string: ")
b = input("Enter a character to remove: ")
result = a.replace(b, "")
print("Resulting string:", result)

# Ask the user for a string and replace all the vowels with a symbol (e.g., *).
a = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""
for char in a:
    if char in vowels:
        result += "*"
    else:
        result += char
print("String with vowels replaced:", result)

"""
Write a program that checks if a string starts with one word and ends with another.
Example:

    Input: "Python is fun!"
    Starts with: "Python"
    Ends with: "fun!"

"""

a = input("Input: ")
start = input("Starts with: ") 
end = input("Ends with: ")
print("Starts with", start, ":", a.startswith(start))
print("Ends with", end, ":", a.endswith(end))