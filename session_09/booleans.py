#!/usr/bin/env python3

#Conditionals are one of the most important aspects of coding
# A Boolean can take on one of two values: True or False
bool1 = type(True)
print(bool1)

#When Boolean have a numeric value, 1 is True, and 0 is False

# Demonstrate Boolean as integer
bool2 = int(True)
print(bool2)
bool3 = int(False)
print(bool3)

# Demonstrate Boolean as float
bool4 = float(True)
print(bool4)
bool5 = float(False)
print(bool5)

# Type cast numeric to Boolean
bool6 = bool(1)
print(bool6)

bool7 = bool(0)
print(bool7)

# Variables
a = 5
b = 10
c = 5

# Determine if values are equal
IsEqual = a == b
print(IsEqual)

# Check if a value is greater than another
IsGreater = a > b
print(IsGreater)

# Check if a value is less than another
IsLess = a < b
print(IsLess)

# Check if a value is less than or equal to another
IsLessOrEqual = a <= c
print(IsLessOrEqual)

# Check if a value is greater than or equal to another
IsGreaterOrEqual = b >= c
print(IsGreaterOrEqual)

# See if values are not equal
IsNotEqual1 = a != b
print(IsNotEqual1)

IsNotEqual2 = a != c
print(IsNotEqual2)

# Check if strings match
str1 = "Hello, World!"
str2 = "Hello, World!"
str3 = "Hello World!"

print(str1 != str2)
print(str1 == str2)
print(str1 != str3)
print(str1 == str2)

# Compare letters
print("A" > "B")
print("A" < "B")
#This is based on the ASCII values
# https://www.ascii-code.com/
# The link above tells you what value a character has
# be careful because letters in Python are case-sensitive

'''
Other Operations to know of
==	equal (since only one = is a variable assignment)
!=	not equal
is	object identity
is not	negated object identity
'''

'''
Logic Operators
"not" "or" "and" all take two values to produce a new Boolean value
You can also use "if, and" or "if, or"
Including "not" in a statement outputs the opposite of the actual value
'''

# Basic logic operators
print(not(True))
print(not(False))

# Using logic operators in a basic conditional
album_year = 1983
if album_year > 1979 and album_year < 1990:
	print("This album was made in the 80’s")
    