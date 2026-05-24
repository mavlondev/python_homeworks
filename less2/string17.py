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