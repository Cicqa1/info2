# print - Print a message to the screen
my_string = "Hello"
print(my_string) # Hello

# input - Read a string from the standard input
my_input = input("Enter a number: ")
print(my_input) # output depends on user input
print("input is:", my_input)  # input is: ---user input---
print(f"input is: {my_input}") # input is: ---user input---

# abs - Return the absolute value of a number
my_number = -10
print(abs(my_number)) # 10

# pow - Return a number raised to the power of another number
my_number = 2
print(pow(my_number, 3)) # 8

# round - Return a number rounded to n digits
my_number = 3.14159
print(round(my_number, 2)) # 3.14

# zip - Return a zip object
my_list1 = [1, 2, 3]
my_list2 = ["a", "b", "c"]
print(list(zip(my_list1, my_list2))) # [(1, 'a'), (2, 'b'), (3, 'c')]

# reversed - Return a reversed iterator
my_list = [1, 2, 3, 4, 5]
print(list(reversed(my_list))) # [5, 4, 3, 2, 1]

# complex - Return a complex number
my_complex = complex(1, 2)
print(my_complex) # (1+2j)

# format - Format a string
my_string = "Hello, {}"
print(my_string.format("World")) # Hello, World

# open - Open a file
my_file = open("example.txt", "r")
print(my_file.read()) # output depends on the content of the file
my_file.close()

# range - Return a sequence of numbers
my_range = range(5)
print(list(my_range)) # [0, 1, 2, 3, 4]

# enumerate - Return an enumerate object
my_list = ["apple", "banana", "cherry"]
print(list(enumerate(my_list))) # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

# divmod - Return the quotient and remainder
my_number1 = 9
my_number2 = 2
print(divmod(my_number1, my_number2)) # (4, 1)

# All - Return True if all elements of the iterable are true
my_list = [True, False, True, True, False]
print(all(my_list)) # False

# Any - Return True if any element of the iterable is true
my_list = [True, False, True, True, False]
print(any(my_list)) # True

# len - Return the length of an object
my_list = [1, 2, 3, 4, 5]
my_string = "Hello"
print(len(my_list)) # 5 
print(len(my_string)) # 5

# min - Return the smallest element
my_list = [1, 2, 3, 4, 5]
my_string = "Hello world i am here_."
my_non_space_string = "maria"
my_list1 = ["giorgi", "george", "mari"]
my_list2 = ["beso", "gio"]
print(min(my_list)) # 1
print(min(my_string)) # " "
print(min(my_non_space_string)) # "a"
print(min(my_list1)) # "george"
print(min(my_list2)) # "beso"

# max - Return the largest element
my_list = [1, 2, 3, 4, 5]
my_string = "Hello world i am here"
my_non_space_string = "hello_world_i_am_here"
my_list1 = ["giorgi", "george", "mari"]
my_list2 = ["beso", "gio"]
print(max(my_list)) # 5
print(max(my_string)) # "w"
print(max(my_non_space_string)) # "w"
print(max(my_list1)) # "mari"
print(max(my_list2)) # "gio"

# sqrt - Return the square root of a number
import math
my_number = 16
print(math.sqrt(my_number)) # 4.0

# ceil - Return the smallest integer greater than or equal to a number
my_number = 3.14
print(math.ceil(my_number)) # 4

# floor - Return the largest integer less than or equal to a number
my_number = 3.14
print(math.floor(my_number)) # 3

# sin - Return the sine of a number
my_number = math.pi / 2
print(math.sin(my_number)) # 1.0

# cos - Return the cosine of a number
my_number = math.pi
print(math.cos(my_number)) # -1.0

# tan - Return the tangent of a number
my_number = math.pi / 4
print(math.tan(my_number)) # 1.0

# log - Return the natural logarithm of a number
my_number = 2
print(math.log(my_number)) # 0.6931471805599453

# exp - Return e raised to the power of a number
my_number = 2
print(math.exp(my_number)) # 7.3890560989306495

# factorial - Return the factorial of a number
my_number = 5
print(math.factorial(my_number)) # 120

# gcd - Return the greatest common divisor of two numbers
my_number1 = 12
my_number2 = 15
print(math.gcd(my_number1, my_number2)) # 3

# pi - Return the value of pi
print(math.pi) # 3.141592653589793

# e - Return the value of e
print(math.e) # 2.718281828459045

# inf - Return positive infinity
print(math.inf) # inf

# nan - Return not a number
print(math.nan) # nan

# random - Generate a random number
import random
print(random.random()) # output varies between 0 and 1

# randint - Generate a random integer
print(random.randint(1, 10)) # output varies between 1 and 10

# choice - Return a random element from a list
my_list = [1, 2, 3, 4, 5]
print(random.choice(my_list)) # output varies between 1 and 5

# shuffle - Shuffle a list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list) # output varies between different permutations of the list

# sample - Return a random sample from a list
my_list = [1, 2, 3, 4, 5]
print(random.sample(my_list, 3)) # output varies between different samples of the list

# time - Return the current time in seconds
import time
print(time.time()) # output varies depending on the current time

# sleep - Pause the program for a specified number of seconds
time.sleep(2) # pause for 2 seconds

# strftime - Format the time
print(time.strftime("%Y-%m-%d %H:%M:%S")) # output varies depending on the current time

# localtime - Return the current time as a struct_time object
print(time.localtime()) # output varies depending on the current time

# calendar - Return a calendar for a specific year and month
import calendar
print(calendar.month(2020, 1)) # output varies depending on the year and month

# isleap - Check if a year is a leap year
print(calendar.isleap(2020)) # True

# leapdays - Return the number of leap years between two years
print(calendar.leapdays(2000, 2020)) # 5