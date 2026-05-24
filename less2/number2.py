# Write a Python file that asks for three numbers and outputs the largest and smallest.

a, b, c = map(int, input().split())
print(f" Largest: {max(a, b, c)}")
print(f" Smallest: {min(a, b, c)}")