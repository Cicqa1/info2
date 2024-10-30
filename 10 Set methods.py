# add - Adds an element to the set 
my_set = {1, 3}
my_set.add(2)
print(my_set) # Output: {1, 2, 3}

# update - Updates the set with another set or any other iterable
my_set = {1, 3, 4}
my_set.update([2, 3, 5])
print(my_set) # Output: {1, 2, 3, 4, 5}

# remove - Removes an element from the set. Raises KeyError if the element is not present
my_set = {1, 3, 4, 5}
my_set.remove(3)
print(my_set) # Output: {1, 4, 5}

# discard - Removes an element from the set if it is present
my_set = {1, 3, 4, 5}
my_set.discard(3)
print(my_set) # Output: {1, 4, 5}

# pop - Removes and returns an arbitrary set element. Raises KeyError if the set is empty
my_set = {1, 3, 4, 5}
print(my_set.pop()) # Output: 1
print(my_set) # Output: {3, 4, 5}

# clear - Removes all elements from the set
my_set = {1, 3, 4, 5}
my_set.clear()
print(my_set) # Output: set()

# difference - Returns the difference of two or more sets as a new set
A = {2, 3, 4, 5}
B = {1, 2, 3}
print(A.difference(B)) # Output: {4, 5}

# intersection - Returns the common elements of two or more sets as a new set
A = {2, 3, 4, 5}
B = {1, 2, 3}
print(A.intersection(B)) # Output: {2, 3}

# union - Returns the union of two sets as a new set
A = {2, 3, 4, 5}
B = {1, 2, 3}
print(A.union(B)) # Output: {1, 2, 3, 4, 5}

# isdisjoint - Returns True if two sets have a null intersection
A = {1, 2, 3}
B = {4, 5, 6}
print(A.isdisjoint(B)) # Output: True

# issubset - Returns True if another set contains this set
A = {1, 2}
B = {1, 2, 3}
print(A.issubset(B)) # Output: True

# issuperset - Returns True if this set contains another set
A = {1, 2, 3}
B = {1, 2}
print(A.issuperset(B)) # Output: True