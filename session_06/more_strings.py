#!/usr/bin/env python3

'''
the code above is referred to a hashbang:
    When you use this in a Python script, the script is marked as an executable,
    and the operating system will use python3 to execute items
'''

# Indexing strings
string_to_index = "Index Arrays" #this is creating the character

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

# Strides
every_2nd_value = string_to_index[::2]
print(every_2nd_value)

complicated_stride = string_to_index[0:5:2]
print(complicated_stride)
#here the syntax is that you are starting with 0, ending at 5, and want every 2nd value

#to find the length of a string use len()
print(len(string_to_index))
#the other function is find()
start_index_Arrays = string_to_index.find("Arrays")
print(start_index_Arrays)

#if the sub-string is not in a string, the output will be -1
not_found = string_to_index.find("I'm not here")
print(not_found)

# Replicating strings
my_bird = "Bird"
total_birds = my_bird * 3
print(total_birds)

# Concatenating strings
#important to note, here my name won't have the space
first_name = "Felisa"
last_name = "Carbajal"
full_name = first_name + last_name
print(full_name)
#fancy way of saying combining

# String formatting
first_name = "Felisa"
last_name = "Carbajal"
print(first_name, last_name)

txt = "Nucleus"
num = 3/11

# Method 1: printf()
print('%s %.3f' % (txt, num))
'''
% is the first element in a string
%.3f
    the 3 means we want to display 3 numbers after the decimal point
    f means the second element is a float
    %d changes things to an integer
    %e changes to scientific notation
    '''
print('%s %.3f %d %e' % (txt, num, 2.1, .1))

# Method 2: str.format()
print('{} {}'.format(txt, num))
print('{} {:.3f}'.format(txt, num))

# Method 3: f-strings
#string interpolation says there can be variables used as placeholders inside a string
# This allows us to put python code inside a string
first_name = "Felisa"
last_name = "Carbajal"

my_first_f_string = f'My first name is {first_name} and my last name is {last_name}. That makes my full name {first_name + " " + last_name}'
print(my_first_f_string)

num = 3/11

decimal_manip = f'The value of 3/11 is {num}. If we round to three decimal places, that makes 3/11 = {num:.3f}'
print(decimal_manip)

'''
general format
my_variable = "variable"
f"Some string with my {my_variable}"
f'Some string with my {my_variable}'

When formatting strings, its better to use the f-string since you can add more information
that will be easier for you to make sense of your code
'''
