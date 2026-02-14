matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])
matrix[0][0] = 10
print(matrix[0][0])

for row in matrix:
    for item in row:
        print(item)
numbers = [1, 2, 3, 4, 5]
numbers2 = numbers.copy()
numbers.append(6) # Add 6 at the end of the list
print(numbers)
numbers.insert(0, 10) # Insert 10 at the beginning (0 meaning the first position)
print(numbers)
numbers.remove(3) # Remove the first occurrence of 3
print(numbers)
numbers.pop() # Remove and return the last item
print(numbers)
print(numbers.index(4)) # Find the index of the first occurrence of 4
print(50 in numbers) # Check if 50 is in the list
print(1 in numbers) # Check if 1 is in the list
print(numbers.count(2)) # Count occurrences of 2
print(numbers.sort()) # Sort the list
print(numbers.reverse()) # Reverse the list
print(numbers.sort()) # Sort the list in place
numbers.clear() # Clear the entire list
print(numbers)

list = [1, 2, 3, 3, 4, 5, 5]
unique_list = list.copy() # this code will create a list with unique elements
for item in list: # this code create a loop to iterate through the original list
    if unique_list.count(item) > 1: # this condition checks if the item appears more than once in the unique_list
        unique_list.remove(item) #this code will remove the item from the unique_list if it appears more than once
print(unique_list)

# alternative way to create a list with unique elements using set:
original_list = [1, 2, 3, 3, 4, 5, 5]
unique = []
if original_list in original_list: # this condition checks if the original_list is in itself
    if original_list not in unique: # this condition checks if the original_list is not already in the unique list
        unique.append(original_list) # this code appends the original_list to the unique list
print(unique)