# Defining two lists with meaningful names
primary_list = [45, 78, "Vimal", True]
secondary_list = [False, "Kumar", 90, 100]

# Inserting a new element into the secondary list
secondary_list.insert(2, "Yadav")

# Extending the primary list with elements from the secondary list
primary_list.extend(secondary_list)

# Printing the updated primary list
print("Updated Primary List:", primary_list)

# Printing the length of the secondary list
print("Length of Secondary List:", len(secondary_list))

# Finding the index of "Yadav" in the secondary list
print("Index of 'Yadav':", secondary_list.index("Yadav"))

# Counting occurrences of "Yadav" in the secondary list
print("Count of 'Yadav':", secondary_list.count("Yadav"))

# Working with a numerical list
numbers = [5, 3, 2, 6, 1]

# Sorting in ascending order, then reversing to get descending order
numbers.sort()
numbers.reverse()

# Creating a copy of the sorted list
numbers_copy = numbers.copy()

# Printing the sorted and reversed list
print("Sorted & Reversed List:", numbers)

# Removing the last element from the copied list
numbers_copy.pop()

# Removing the first element from the copied list
del numbers_copy[0]

# Printing the modified copy
print("Modified Copy:", numbers_copy)
