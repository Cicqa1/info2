# "if" - if statement
a = 33
b = 200
if b > a:
  print("b is greater than a")  # Output: "b is greater than a"

# "elif" - else if statement
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
    print("a and b are equal")  # Output: "a and b are equal"

# "else" - else statement
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")  # Output: "a is greater than b"

# "not" - not operator
a = True
print(not a)  # Output: False

# "if" "if" "elif" "else" "not" - if, elif, else, and not statements
a = 200
b = 33
if a < b:
    print("a is less than b")
    if a == b:
        print("a and b are equal")
    elif a > b:
        print("a is greater than b")
else:
    print("a is greater than b")
    if not a == b:
        print("a and b are not equal")  # Output: "a is greater than b" "a and b are not equal"
