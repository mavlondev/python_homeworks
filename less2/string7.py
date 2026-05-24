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