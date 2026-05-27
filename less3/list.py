# 1. **Count Occurrences**: Given a list and an element, find how many times the element appears in the list.
arr = list(map(int, input().split()))
element = int(input())
print(arr.count(element))

# 2. **Sum of Elements**: Given a list of numbers, calculate the total of all the elements.
arr = list(map(int, input().split()))
print(sum(arr))

# 3. **Max Element**: From a given list, determine the largest element.
arr = list(map(int, input().split()))
print(max(arr))

# 4. **Min Element**: From a given list, determine the smallest element.
arr = list(map(int, input().split()))
print(min(arr))

# 5. **Check Element**: Given a list and an element, check if the element is present in the list.
arr = list(map(int, input().split()))
element = int(input())
print(element in arr)

# 6. **First Element**: Access the first element of a list, considering what to return if the list is empty.
arr = list(map(int, input().split()))
if arr:
    print(arr[0])
else:
    print("List is empty")

# 7. **Last Element**: Access the last element of a list, considering what to return if the list is empty.
arr = list(map(int, input().split()))
if arr:
    print(arr[-1])
else:
    print("List is empty")

# 8. **Slice List**: Create a new list that contains only the first three elements of the original list.
arr = list(map(int, input().split()))
print(arr[:3])

# 9. **Reverse List**: Create a new list that contains the elements of the original list in reverse order.
arr = list(map(int, input().split()))
print(arr[::-1])

# 10. **Sort List**: Create a new list that contains the elements of the original list in sorted order.
arr = list(map(int, input().split()))
print(sorted(arr))

# 11. **Remove Duplicates**: Given a list, create a new list that contains only unique elements from the original list.
arr = list(map(int, input().split()))
unique_arr = []
for i in arr:
    if i not in unique_arr:
        unique_arr.append(i)
print(unique_arr)

# 12. **Insert Element**: Given a list and an element, insert the element at a specified index.
arr = list(map(int, input().split()))
element = int(input())
index = int(input())
arr.insert(index, element)
print(arr)

# 13. **Index of Element**: Given a list and an element, find the index of the first occurrence of the element.
arr = list(map(int, input().split()))
element = int(input())
print("arr is empty" if element not in arr else arr.index(element))

# 14. **Check for Empty List**: Determine if a list is empty and return a boolean.
arr = list(map(int, input().split()))
print(len(arr) == 0)

# 15. **Count Even Numbers**: Given a list of integers, count how many of them are even.
arr = list(map(int, input().split()))
even_count = 0
for i in arr:
    even_count += i%2==0
print(even_count)

# 16. **Count Odd Numbers**: Given a list of integers, count how many of them are odd.
arr = list(map(int, input().split()))
odd_count = 0
for i in arr:
    odd_count += i%2
print(odd_count)

# 17. **Concatenate Lists**: Given two lists, create a new list that combines both lists.
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
combined_list = list1 + list2
print(combined_list)

# 18. **Find Sublist**: Given a list and a sublist, check if the sublist exists within the list.
arr = list(map(int, input().split()))
sublist = list(map(int, input().split()))

# ????????????????????????


# 19. **Replace Element**: Given a list, replace the first occurrence of a specified element with another element.
arr = list(map(int, input().split()))
specified_element = int(input())
replacement_element = int(input())
arr[arr.index(specified_element)] = replacement_element
print(arr)

# 20. **Find Second Largest**: From a given list, find the second largest element.
arr = list(set(map(int, input().split())))
print(arr[-2])

# 21. **Find Second Smallest**: From a given list, find the second smallest element.
arr = list(set(map(int, input().split())))
print(arr[1])

# 22. **Filter Even Numbers**: Given a list of integers, create a new list that contains only the even numbers.
arr = list(map(int, input().split()))
new_arr = list(filter(lambda x: x%2==0, arr))
print(new_arr)

# 23. **Filter Odd Numbers**: Given a list of integers, create a new list that contains only the odd numbers.
arr = list(map(int, input().split()))
new_arr = list(filter(lambda x: x%2==1, arr))
print(new_arr)

# 24. **List Length**: Determine the number of elements in the list.
print(len(list(map(int, input().split()))))

# 25. **Create a Copy**: Create a new list that is a copy of the original list.
from copy import deepcopy
arr = list(map(int, input().split()))
copy_arr = deepcopy(arr)
print(copy_arr)

# 26. **Get Middle Element**: Given a list, find the middle element. If the list has an even number of elements, return the two middle elements.
arr = list(map(int, input().split()))
length = len(arr)
if length % 2 == 1: 
    print(arr[length // 2])
else:
    print(arr[length // 2 - 1], arr[length // 2])

# 27. **Find Maximum of Sublist**: Given a list, find the maximum element of a specified sublist.

# ????????????????????????

# 28. **Find Minimum of Sublist**: Given a list, find the minimum element of a specified sublist.

# ????????????????????????

# 29. **Remove Element by Index**: Given a list and an index, remove the element at that index if it exists.
arr = list(map(int, input().split()))
index = int(input())
if 0 <= index < len(arr):
    arr.pop(index)
print(arr)

# 30. **Check if List is Sorted**: Determine if the list is sorted in ascending order and return a boolean.

arr = list(map(int, input().split()))
sorted_arr = sorted(arr)
print(arr == sorted_arr)

# 31. **Repeat Elements**: Given a list and a number, create a new list where each element is repeated that number of times.
arr = list(map(int, input().split()))
number = int(input())
new_arr = []
for i in arr:
    new_arr.extend([i] * number)
print(new_arr)

# 32. **Merge and Sort**: Given two lists, create a new sorted list that merges both lists.
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
merged_arr = sorted(arr1 + arr2)
print(merged_arr)

# 33. **Find All Indices**: Given a list and an element, find all the indices of that element in the list.
arr = list(map(int, input().split()))
element = int(input())
indices = [i for i, x in enumerate(arr) if x == element]
print(indices)

# 34. **Rotate List**: Given a list, create a new list that is a rotated version of the original list (shift elements to the right).
arr = list(map(int, input().split()))
rotated_arr = [arr[-1]] + arr[:-1]
print(rotated_arr)


# 35. **Create Range List**: Create a list of numbers in a specified range (e.g., from 1 to 10).

start = int(input())
end = int(input())
range_list = list(range(start, end + 1))
print(range_list)

# 36. **Sum of Positive Numbers**: Given a list of numbers, calculate the sum of all positive numbers.

arr = list(map(int, input().split()))
positive_sum = sum(x for x in arr if x > 0)
print(positive_sum)

# 37. **Sum of Negative Numbers**: Given a list of numbers, calculate the sum of all negative numbers.
arr = list(map(int, input().split()))
negative_sum = sum(x for x in arr if x < 0)
print(negative_sum)

# 38. **Check Palindrome**: Given a list, check if the list is a palindrome (reads the same forwards and backwards).
arr = list(map(int, input().split()))
is_palindrome = arr == arr[::-1]
print(is_palindrome)

# 39. **Create Nested List**: Create a new list that contains sublists, where each sublist contains a specified number of elements from the original list.

# ????????????????????????

# 40. **Get Unique Elements in Order**: Given a list, create a new list that contains unique elements while maintaining the original order.
arr = list(map(int, input().split()))
unique_ordered_arr = []
for i in arr:
    if i not in unique_ordered_arr:
        unique_ordered_arr.append(i)
print(unique_ordered_arr)
