# lower - Convert to lowercase
my_string = "Hello"
print(my_string.lower()) # hello

# upper - Convert to uppercase
my_string = "Hello"
print(my_string.upper()) # HELLO

# capitalize - Capitalize the first letter
my_string = "hello, world"
print(my_string.capitalize()) # Hello, world

# find - Find a substring
my_string = "Hello, World"
print(my_string.find("World")) # 7

# min - Return the smallest element
my_list = [1, 2, 3, 4, 5]
my_string = "Hello world i am here"
my_nonspace_string = "helloworldiamhere"
print(min(my_list)) # 1
print(min(my_string)) # " "
print(min(my_nonspace_string)) # "a"

# max - Return the largest element
my_list = [1, 2, 3, 4, 5]
my_string = "Hello world i am here"
my_nonspace_string = "helloworldiamhere"
print(max(my_list)) # 5
print(max(my_string)) # "w"
print(max(my_nonspace_string)) # "w"

# replace - Replace a substring
my_string = "Hello, World"
print(my_string.replace("World", "Python")) # Hello, Python

# split - Split the string into a list
my_string = "Hello, World"
print(my_string.split(", ")) # ['Hello', 'World']

# join - Join a list into a string
my_list = ["Hello", "World"]
print(", ".join(my_list)) # Hello, World

# startswith - Check if the string starts with a substring
my_string = "Hello, World"
print(my_string.startswith("Hello")) # True

# endswith - Check if the string ends with a substring
my_string = "Hello, World"
print(my_string.endswith("!")) # False

# count - Count the occurrences of a substring
my_string = "Hello, World"
print(my_string.count("o")) # 2

# index - Return the index of a substring
my_string = "Hello, World"
print(my_string.index("W")) # 7

# splitlines - Split the string into a list of lines
my_string = "Hello\nWorld"
print(my_string.splitlines()) # ['Hello', 'World']

# strip - Remove leading and trailing characters
my_string = "  Hello  "
print(my_string.strip()) # Hello

# lstrip - Remove leading characters
my_string = "  Hello  "
print(my_string.lstrip()) # Hello

# rstrip - Remove trailing characters
my_string = "  Hello  "
print(my_string.rstrip()) #   Hello

# zfill - Pad the string with zeros
my_string = "Hello"
print(my_string.zfill(10)) # 00000Hello

# title - Convert the first character of each word to uppercase
my_string = "hello, world"
print(my_string.title()) # Hello, World

# swapcase - Swap the case of the string
my_string = "Hello, World"
print(my_string.swapcase()) # hELLO, wORLD

# center - Center the string
my_string = "Hello"
print(my_string.center(10)) #   Hello

# encode - Encode the string
my_string = "Hello"
print(my_string.encode()) # b'Hello'

# expandtabs - Expand the tabs in the string
my_string = "Hello\tWorld"
print(my_string.expandtabs(4)) # Hello   World

# isalnum - Return True if all characters are alphanumeric
my_string = "Hello"
print(my_string.isalnum()) # True

# isalpha - Return True if all characters are alphabetic
my_string = "Hello"
print(my_string.isalpha()) # True

# isdigit - Return True if all characters are digits
my_string = "123"
print(my_string.isdigit()) # True

# islower - Return True if all characters are lowercase
my_string = "hello"
print(my_string.islower()) # True

# isupper - Return True if all characters are uppercase
my_string = "HELLO"
print(my_string.isupper()) # True

# isnumeric - Return True if all characters are numeric
my_string = "123"
print(my_string.isnumeric()) # True

# isspace - Return True if all characters are whitespace
my_string = "   "
print(my_string.isspace()) # True

# isprintable - Return True if all characters are printable
my_string = "Hello"
print(my_string.isprintable()) # True

# isidentifier - Return True if the string is a valid identifier
my_string = "Hello"
print(my_string.isidentifier()) # True

# isascii - Return True if all characters are ASCII
my_string = "Hello"
print(my_string.isascii()) # True

# isdecimal - Return True if all characters are decimal
my_string = "123"
print(my_string.isdecimal()) # True

# isdigit - Return True if all characters are digits
my_string = "123"
print(my_string.isdigit()) # True

# isnumeric - Return True if all characters are numeric
my_string = "123"
print(my_string.isnumeric()) # True

# rjust - Right-justify the string
my_string = "Hello"
print(my_string.rjust(10)) # Hello

# ljust - Left-justify the string
my_string = "Hello"
print(my_string.ljust(10)) # Hello

# partition - Partition the string
my_string = "Hello, World"
print(my_string.partition(", ")) # ('Hello', ', ', 'World')

# rpartition - Partition the string from the right
my_string = "Hello, World"
print(my_string.rpartition(", ")) # ('Hello', ', ', 'World')

# translate - Translate the string
my_string = "Hello"
table = my_string.maketrans("H", "J")
print(my_string.translate(table)) #

# format - Format the string
my_string = "Hello, {}"
print(my_string.format("World")) # Hello, World

# center - Center the string
my_string = "Hello"
print(my_string.center(10)) #   Hello

# splitlines - Split the string into a list of lines
my_string = "Hello\nWorld"
print(my_string.splitlines()) # ['Hello', 'World']