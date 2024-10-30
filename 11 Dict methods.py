# get - returns the value of the specified key. If the key does not exist, it returns None or the specified default value.
my_dict = {'name': 'Jack', 'age': 26}
print(my_dict.get('name'))  # Output: Jack
print(my_dict.get('age'))  # Output: 26
print(my_dict.get('address'))  # Output: None
print(my_dict.get('address', 'Not Found'))  # Output: Not Found

# items - returns a new view of the dictionary items (key, value).
my_dict = {'name': 'Jack', 'age': 26}
print(my_dict.items())  # Output: dict_items([('name', 'Jack'), ('age', 26)])

# keys - returns a new view of the dictionary keys.
my_dict = {'name': 'Jack', 'age': 26}
print(my_dict.keys())  # Output: dict_keys(['name', 'age'])

# values - returns a new view of the dictionary values.
my_dict = {'name': 'Jack', 'age': 26}
print(my_dict.values())  # Output: dict_values(['Jack', 26])

# pop - removes the item with the specified key and returns the value.
my_dict = {'name': 'Jack', 'age': 26}
print(my_dict.pop('name'))  # Output: Jack
print(my_dict)  # Output: {'age': 26}

# popitem - removes the last inserted item.
my_dict = {'name': 'Jack', 'age': 26}
print(my_dict.popitem())  # Output: ('age', 26)
print(my_dict)  # Output: {'name': 'Jack'}

# setdefault - returns the value of the specified key. If the key does not exist, insert the key, with the specified value.
my_dict = {'name': 'Jack', 'age': 26}
print(my_dict.setdefault('name'))  # Output: Jack
print(my_dict.setdefault('address'))  # Output: None

# update - updates the dictionary with the specified key-value pairs.
my_dict = {'name': 'Jack', 'age': 26}
my_dict.update({'age': 27})
print(my_dict)  # Output: {'name': 'Jack', 'age': 27}
my_dict.update({'address': 'Downtown'})
print(my_dict)  # Output: {'name': 'Jack', 'age': 27, 'address': 'Downtown'}

# clear - removes all the elements from the dictionary.
my_dict = {'name': 'Jack', 'age': 26}
my_dict.clear()
print(my_dict)  # Output: {}

# copy - returns a copy of the dictionary.
my_dict = {'name': 'Jack', 'age': 26}
my_dict_copy = my_dict.copy()
print(my_dict_copy)  # Output: {'name': 'Jack', 'age': 26}