#!/usr/bin/env python3

print("Problem 1:")
#Fixed the issue by making sure the "" was at the end and the ' is in the middle to not
#confuse python
print("Anthony J. D'Angelo said, 'Develop a passion for learning. If you do, you will never cease to grow.'")

print("Problem 2:")
#Make the following sentence appear completely uppercase:
# The door swung open to reveal pink giraffes and red elephants.
number2 = "The door swung open to reveal pink giraffes and red elephants."
number2_1 = number2.upper()
print(number2_1)
# the syntax here is to include the function we want done to the string at the end

print("Problem 3:")
#Determine the index of the "a" in "departure."
problem_3 = "departure"
find_a = problem_3[3]
print(find_a)
# Remember for indexes they start at zero, the first letter is zero

print("Problem 4:")
# Determine the length of the sentence: 
#The tattered work gloves speak of the many hours of hard labor he endured throughout his life
problem_4 = "The tattered work gloves speak of the many hours of hard labor he endured throughout his life"
problem_4_ans = len(problem_4)
print(problem_4_ans)

print("Problem 5:")
# Given a variable breed = "Great Dane", use string formatting (e.g. f-string) to print the following sentence: The Great Dane looked more like a horse than a dog.
breed = "Great Dane"
problem_5 = f'The {breed} looked more like a horse than a dog.'
print(problem_5)


print("Problem 6:")
# Assign breed to "Mastiff" and reprint the statement.
breed = "Mastiff"
print(f'The {breed} looked more like a horse than a dog.')
