#!/usr/bin/env python3

'''
the code above is referred to a hashbang:
    When you use this in a Python script, the script is marked as an executable,
    and the operating system will use python3 to execute items
'''

# Indexing strings
string_to_index = "Index Arrays"

first_A = string_to_index[6]
print(first_A)

first_word = string_to_index[0:5]
print(first_word)

last_word = string_to_index[6:12]
print(last_word)

'''
when we use the range function, it is different than with R, it doesn't do
range from start to end, it does [start index, total elements]
a good way to think about it is: [start index, end index + 1]
'''
last_index = string_to_index[-1]
print(last_index)
