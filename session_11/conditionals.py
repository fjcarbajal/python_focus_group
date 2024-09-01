#!/usr/bin/env python3


#Conditionals (if-Else Statements) are when an action will be taken only if your data meets a certain condition
# Conditionals are a powerful tool in bioinformatics
age = 17

if age >= 18:
    print("You may enter!")
else:
    print("You are too young to enter.")
    
'''
In general, this is the formatting for if-else statements
if {some condition}:
    {code to execute}
else:
    {alternative code to execute if the condition is not met}
'''
age = 14
print("Dad: Happy birthday! How old are you turning this year?")
print(f"Son: Thank you. I’m turning {age} this year")
if age >= 16:
	print("Dad: Good, now go get a job")
else:
	print(f"Dad: Wow, only {16-age} more years until you can get a job")
    
x = 10
y = 10

if x > y:
    print("x is greater than y")
elif x < y: #Consider this as if it doesn't match the first condition, does it match this..
    print("x is less than y")
else:
    print("x is equal to y")
    
#using "and" conditionals means BOTH combinations must be satisfied to move forward
age = 20

if age >= 18 and age < 21:
    print("You may enter!")
else:
    print("This club is not for you.")

age = 17

if age >= 18 and age < 21:
    print("You may enter!")
elif age < 18:
    print("You're too young!")
else:
    print("This club is not for you.")
    
#Using "or" is when only one of the conditions need to be met
marble = "green"

if marble == "blue" or marble == "green":
    print("Yay! This is one of my favorite colors.")
else:
    print("Oh no, I wanted a different color.")
    
marble = "blue"

if marble == "blue" and marble == "green":
    print("Yay! This is one of my favorite colors.")
else:
    print("Oh no, I wanted a different color.")
    
my_pets = ["Iguana", "Gecko", "Bird"]
# You don't always need to have an else statement in your conditionals
if "Gecko" in my_pets:
    print("Ooh! Viki has a gecko!")
    
print("We have now passed the conditional")

my_pets = ["Iguana", "Bird"]
#Here your conditional will not be met but without an "else" portion,
#The code continues without this part
if "Gecko" in my_pets:
    print("Ooh! Viki has a gecko!")

print("We have now passed the conditional")

# Original list
my_numbers = [74, 60, 4, 93, 2, 1, 54]

# New lists
single_digits = []
double_digits = []

for num in my_numbers:
    if num < 10:
        single_digits.append(num)
    else:
        double_digits.append(num)

print(single_digits)
print(double_digits)

#Another way to do the same thing
# Original list
my_numbers = [74, 60, 4, 93, 2, 1, 54]

# New lists
single_digits = []
double_digits = []

for num in my_numbers:
    # Convert the number to a string to assess length
    num = str(num)
    if len(num) == 1:
        single_digits.append(int(num))
    else:
        double_digits.append(int(num))

print(single_digits)
print(double_digits)
#I prefer the first way of doing this example