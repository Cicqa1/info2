# "and" - both conditions must be true
a = 10
b = 20
if a > 5 and b > 15:
  print("Both conditions are true")  # Output: "Both conditions are true"

name = "Alice"
age = 25
if name == "Alice" and age == 25:
  print("Name is Alice and age is 25")  # Output: "Name is Alice and age is 25"
else:
  print("Name is not Alice or age is not 25")  # Output: "Name is not Alice or age is not 25"

# "or" - at least one condition must be true
a = 10
b = 20
if a > 5 or b > 15:
  print("At least one condition is true")  # Output: "At least one condition is true"

name = "Alice"
age = 25
if name == "Alice" or age == 30:
  print("Name is Alice or age is 30")  # Output: "Name is Alice or age is 30"
else:
  print("Name is not Alice and age is not 30")

# "not" - reverse the result, returns False if the result is true
a = 10
b = 20
if not a > 5:
  print("a is not greater than 5")  # Output: None
else:
  print("a is greater than 5")

name = "Alice"
age = 25
if not name == "Alice":
  print("Name is not Alice")  # Output: None 
else:
  print("Name is Alice")

# "in" - returns True if a sequence with the specified value is present in the object
my_list = [1, 2, 3, 4, 5]
if 3 in my_list:
  print("3 is present in the list")  # Output: "3 is present in the list"
my_string = "Hello, World"
if "Hello" in my_string:
  print("Hello is present in the string")  # Output: "Hello is present in the string"

# "not in" - returns True if a sequence with the specified value is not present in the object
my_list = [1, 2, 3, 4, 5]
if 6 not in my_list:
  print("6 is not present in the list")  # Output: "6 is not present in the list"
my_string = "Hello, World"
if "Python" not in my_string:
  print("Python is not present in the string")  # Output: "Python is not present in the string"

# "is" - returns True if both variables are the same object
a = 10
b = a
if a is b:
  print("a and b are the same object")  # Output: "a and b are the same object"
my_list1 = [1, 2, 3]
my_list2 = my_list1
if my_list1 is my_list2:
  print("my_list1 and my_list2 are the same object")  # Output: "my_list1 and my_list2 are the same object"

# "is not" - returns True if both variables are not the same object
a = 10
b = 20
if a is not b:
  print("a and b are not the same object")  # Output: "a and b are not the same object"
my_list1 = [1, 2, 3]
my_list2 = [1, 2, 3]
if my_list1 is not my_list2:
  print("my_list1 and my_list2 are not the same object")  # Output: "my_list1 and my_list2 are not the same object"

# "pass" - used as a placeholder
a = 10
b = 20
if a > b:
  pass
else:
  print("a is not greater than b")
name = "Alice"
age = 25
if name == "Alice":
  pass
else:
  print("Name is not Alice")

# "break" - exit the loop
my_list = [1, 2, 3, 4, 5]
for number in my_list:
  if number == 3:
    break
  print(number)  # Output: 1 2

# "continue" - skip the current iteration and continue with the next one
my_list = [1, 2, 3, 4, 5]
for number in my_list:
  if number == 3:
    continue
  print(number)  # Output: 1 2 4 5

# "assert" - raise an AssertionError if the condition is false
a = 10
b = 20
assert a < b
print("a is less than b")  # Output: "a is less than b"
name = "Alice"
age = 25
assert name == "Alice"
print("Name is Alice")  # Output: "Name is Alice"

# "del" - delete an object
a = 10
b = 20
del a
# print(a)  # Output: NameError: name 'a' is not defined
my_list = [1, 2, 3, 4, 5]
del my_list

# "def" - define a function
def my_function():
	print("Hello from a function")

my_function()  # Output: "Hello from a function"

# def function with arguments
def my_function(name, surname):
  print(f"name is {name}, surname is {surname}")
my_function("Alice", "Smith")   # Output: "name is Alice, surname is Smith"

