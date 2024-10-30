# "for" - is used to iterate over a sequence (list, tuple, string) or other iterable objects.
values = [1, 2, 3, 4, 5]
for value in values:
    print(value) # 1 2 3 4 5

# "for" loop can be used to iterate over a string.
for letter in "Hello":
    print(letter) # H e l l o

# "for" loop can be used to iterate over a tuple.
for number in (1, 2, 3, 4, 5):
    print(number) # 1 2 3 4 5

# "for" loop can be used to iterate over a dictionary.
person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(key, person[key]) # name John age 30 city New York

# "for" loop can be used to iterate over a range of numbers.
for number in range(5):
    print(number) # 0 1 2 3 4

# "for" loop can be used to iterate over a range of numbers with a start and end value.
for number in range(2, 5):
    print(number) # 2 3 4

# "for" loop can be used to iterate over a range of numbers with a start, end and step value.
for number in range(1, 10, 2):
    print(number) # 1 3 5 7 9

# "for" loop can be used to iterate over a range of numbers in reverse order.
for number in range(5, 0, -1):
    print(number) # 5 4 3 2 1
