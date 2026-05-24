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