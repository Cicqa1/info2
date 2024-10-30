# append - Adds an element at the end of the list
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list) # [1, 2, 3, 4, 5, 6]

# extend - Adds all elements of a list to another list
my_list = [1, 2, 3, 4, 5]
my_list.extend([6, 7, 8])
print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8]


# insert - Inserts an element at a specific position
my_list = [1, 2, 3, 4, 5]  
my_list.insert(2, 6)
print(my_list) # [1, 2, 6, 3, 4, 5]

# remove - Removes the first occurrence of an element
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list) # [1, 2, 4, 5]

# pop - Removes and returns the last element
my_list = [1, 2, 3, 4, 5]
print(my_list.pop()) # 5
print(my_list) # [1, 2, 3, 4]

# clear - Removes all elements from the list
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list) # []

# index - Returns the index of the first occurrence of an element
my_list = [1, 2, 3, 4, 5]  
print(my_list.index(3)) # 2

# count - Returns the number of occurrences of an element
my_list = [1, 2, 3, 4, 5, 3]
print(my_list.count(3)) # 2

# sort - Sorts the list in ascending order
my_list = [3, 2, 1, 5, 4]
my_list.sort()
print(my_list) # [1, 2, 3, 4, 5]

# reverse - Reverses the elements of the list
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list) # [5, 4, 3, 2, 1]

# copy - Returns a shallow copy of the list
my_list = [1, 2, 3, 4, 5]
copied_list = my_list.copy()
print(copied_list) # [1, 2, 3, 4, 5]

# join - Joins the elements of a list into a string
my_list = ["Hello", "World", "!"]
print(" ".join(my_list)) # "Hello World !"