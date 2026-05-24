# Write a program that counts the number of vowels and consonants in a given string
a = input("Enter a string: ")
vowels = "aeiou"
vowel_count = 0
for char in a.lower():
    if char in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count) 
print("Number of consonants:", len(a) - vowel_count)