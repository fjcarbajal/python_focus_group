#!/usr/bin/env python3

'''
Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''

# Examples of strings
str1 = "Hello world"
str2 = "Spring is coming!"
str3 = "My dog ate 3 slices of my pizza"
str4 = "I can't believe my dog did that"

#You can overwrite functions
#str() is a function so don't name anything as str = 

# String operations
original_str = "Viki is teaching me how to code in Python"

upper_str = original_str.upper()
print(upper_str)

title_str = original_str.title()
print(title_str)

lower_str = original_str.lower()
print(lower_str)

replace_str = original_str.replace("Viki", "The internet")
print(replace_str)

# Stripping spaces
spaced_out = " M y N a m e I s V i k i "
right_strip = spaced_out.rstrip()
left_strip = spaced_out.lstrip()

print(right_strip)
print(left_strip)

#In Python, strings are considered objects
# When dealing with objects, the syntax is function comes after the variable
# Ex) upper_str.replace the function (replace) comes after the object
# And since the functions we were learning (upper, lower) they are specific to strings
# Then we follow object syntax and put the function afterwards

# Google if you don't know if you are working with objects or other data types