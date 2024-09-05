#!/usr/bin/env python3

# Create a function
def greeting():
    print("Hello, world!")
    
# Call function
greeting()

# When creating a function, you need to start with def
# This lets Python know that you are about to create a function

# Create a function with argument 'some_string'
def add_underscore(some_string): #remember to have a descriptive function name followed by your argument
    new_string = some_string + "_" #the definition of your argument?
    print(new_string)

# Call function
add_underscore("Viki")

def add_numbers(number1, number2):
    my_sum = number1 + number2
    print(my_sum)

add_numbers(3, 7)


# Create a function that prints the first letter (initial) of each input name
def first_letters(*names): #you add the * when you don't have a set number of arguments
    for name in names:
        print(name[0])

first_letters("Bijoy", "Helen", "Miley", "Roxanna", "Felisa", "Abraham", "Adam")

def my_kids(child3, child2, child1):
    print("The youngest child is " + child3)
    
my_kids("Emily", "Tobias", "Linus")
my_kids(child1 = "Emily", child2 = "Tobias", child3 = "Linus") 
#When you don't specify your variables, then Python will make assumptions based
#on how the function was written
#In this example, python assumes child3 was Emily until we specified

def my_home(country = "USA"): #we have set a default argument
    print("I am from " + country)
    
my_home("Sweden")
my_home("Lebanon")
my_home() #we have not specified an argument so python resorts to the default
#Setting defaults can be helpful when we are working in complicated situations

def associate_ages(a_dictionary):
    for name, age in a_dictionary.items(): #Notice the syntax for this dictionary, since you are calling on your dictionary
        print(f'{name} is {age} years old.')

ages = {"Viki": 25, "Logan": 25, "Osman": 30}
associate_ages(ages)
#Functions can have any data type as long as you properly define them

# Original
print("Here, we are testing the original function")
def add_numbers(number1, number2):
    my_sum = number1 + number2
    print(my_sum)
    
my_var = add_numbers(3, 7)
print("My variable: ", my_var) #

# With Return
print("Here, we are testing the rewritten function")
def add_numbers(number1, number2):
    my_sum = number1 + number2
    return my_sum
# when you use return() and not print(),
# you can store the final value and use it in a separate function
my_var = add_numbers(3, 7)
print("My variable: ", my_var)

# Original
def add_numbers(number1, number2):
    my_sum = number1 + number2
    print(my_sum)

# With Return
def add_numbers(number1, number2):
    my_sum = number1 + number2
    return my_sum
    
def empty_function():
    pass #you have to write "pass" if you are creating an empty function
#function bodies can not be empty

a = empty_function()
print(a)

#A recursive function is one that calls on itself
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results")
tri_recursion(6)
#Still a bit confused on how recursive functions work

# Create function with a description
def add1(a): #THIS IS SUPER USEFUL
    """
    Add 1 to a
    """
    b = a + 1
    return b
# Execute function
add1(5)

help(add1)