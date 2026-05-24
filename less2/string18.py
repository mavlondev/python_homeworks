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