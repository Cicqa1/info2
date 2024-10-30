# type - Return the type of an object
my_integer = 10
my_float = 1.5
my_string = "Hello"
my_boolean = True
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5) 
my_dict = {"name": "John", "age": 36}
my_set = {1, 2, 3, 4, 5}
print(type(my_integer)) # <class 'int'>
print(type(my_float)) # <class 'float'>
print(type(my_string)) # <class 'str'>
print(type(my_boolean)) # <class 'bool'>
print(type(my_list)) # <class 'list'>
print(type(my_tuple)) # <class 'tuple'>
print(type(my_dict)) # <class 'dict'>
print(type(my_set)) # <class 'set'>

# int - Convert a number or string to an integer
my_number = 3.14
my_string = "10"
print(int(my_number)) # 3
print(int(my_string)) # 10

# float - Convert a number or string to a float
my_number = 10
my_string = "3.14"
print(float(my_number)) # 10.0
print(float(my_string)) # 3.14

# str - Convert an object to a string
my_number = 10
my_list = [1, 2, 3, 4, 5]
my_dict = {"name": "John", "age": 36}
print(str(my_number)) # 10
print(str(my_list)) # [1, 2, 3, 4, 5]
print(str(my_dict)) # {'name': 'John', 'age': 36}

# bool - Convert an object to a boolean
my_number = 10
my_string = "Hello"
my_list = [1, 2, 3, 4, 5]
my_dict = {"name": "John", "age": 36}
print(bool(my_number)) # True
print(bool(my_string)) # True
print(bool(my_list)) # True
print(bool(my_dict)) # True

# list - Convert an object to a list
my_string = "Hello"
my_tuple = (1, 2, 3, 4, 5)
my_set = {1, 2, 3, 4, 5}
my_dict = {"name": "John", "age": 36}
print(list(my_string)) # ['H', 'e', 'l', 'l', 'o']
print(list(my_tuple)) # [1, 2, 3, 4, 5]
print(list(my_set)) # [1, 2, 3, 4, 5]
print(list(my_dict)) # ['name', 'age']

# tuple - Convert an object to a tuple
my_string = "Hello"
my_list = [1, 2, 3, 4, 5]
my_set = {1, 2, 3, 4, 5}
my_dict = {"name": "John", "age": 36}
print(tuple(my_string)) # ('H', 'e', 'l', 'l', 'o')
print(tuple(my_list)) # (1, 2, 3, 4, 5)
print(tuple(my_set)) # (1, 2, 3, 4, 5)
print(tuple(my_dict)) # ('name', 'age')

# set - Convert an object to a set
my_string = "Hello"
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_dict = {"name": "John", "age": 36}
print(set(my_string)) # {'H', 'e', 'l', 'o'}
print(set(my_list)) # {1, 2, 3, 4, 5}
print(set(my_tuple)) # {1, 2, 3, 4, 5}
print(set(my_dict)) # {'name', 'age'}

# dict - Convert an object to a dictionary
my_list = [("name", "John"), ("age", 36)]
my_tuple = (("name", "John"), ("age", 36))
my_set = {("name", "John"), ("age", 36)}
print(dict(my_list)) # {'name': 'John', 'age': 36}
print(dict(my_tuple)) # {'name': 'John', 'age': 36}
print(dict(my_set)) # {'name': 'John', 'age': 36}