#!/usr/bin/env python3

'''
For-loop function are like saying "for every item, do this action"
'''

# Make a list
magicians = ["alice", "david", "carolina"]

# Printing the list to see the magicians
print(magicians)

# Printing each magician individually
for magician in magicians:
	print(magician)    

# Carry out more complicated actions
for magician in magicians:
	print(magician.title() + " , that was a great trick!")
	print("I can’t wait to see your next trick, " + magician.title() + ".\n")

# Carry out more complicated actions
for magician in magicians:
	print(magician.title() + " , that was a great trick!")
	print("I can’t wait to see your next trick, " + magician.title() + ".\n")
	
print("Thank you, everyone. That was a great magic show!")
#To do something after a for-loop make sure its not indented

# More basic for-loops
A = [1, 2, 3, 4, 5]
for value in A:
    print(value)
	
dates = [1982, 1980, 1973]
for date in dates:
    print(date)
	
# A more complicated for-loop where you can access the index and list items
x = len(dates) #len is function for length
for i in range(x):
    print(i, dates[i])  
#The above lets you see what date is at what index
	
# The range() function
squares = [] #creates an empty list named squares, the square of each number will be stored here
for value in range(1,11): #your range of numbers 1-10 *remember index!!!**
	square = value**2 #what happens to each value (gets squared)
	squares.append(square) #add that squared value to the "squares" list
print(squares) #prints the "squares" list

#Nesting means to put a for-loop inside a for-loop
# Nested for-loop
groupA = ["Janine", "Jessica", "Jules"]
groupB = ["Osman", "Dag", "Logan"]

for person1 in groupA:
	for person2 in groupB:
		print(person1, person2)
        
# By doing this, you can look at all combinations of variables
# this is good when you have a dataset with nested metadata
# Viki's Project Set-Up
sexes = ["male", "female"]
genotypes = ["WT", "MUT"]
time_points = ["E18", "P30", "P60", "P120"]
cell_types = ["Camk2a", "VIP"]

print("All conditions for Viki's project:")
for sex in sexes:
	for genotype in genotypes:
		for time_point in time_points:
			for cell_type in cell_types:
				print(sex, genotype, time_point, cell_type)

# Parallel for-loop
listA = [1, 2, 3, 4, 5]
listB = ["A", "B", "C", "D", "E"]

for A, B in zip(listA, listB):
	print(f'Variable A is {A} and variable B is {B}. Here is AB: {A}{B}')

# Rename variables
for something1, something2 in zip(listA, listB):
	print(something1, something2)

# Switch the order of the lists
for A, B in zip(listB, listA):
	print(A, B)

#This biggest thing to remember here is the order of how you zip() the two datasets


ages = {"Viki": 24, "Logan": 25, "Osman": 30}

# Access keys only
for name in ages.keys():
	print(name)

# Access values only
for age in ages.values():
	print(age)

# Access keys and values
for name, age in ages.items():
	print(f'{name} is {age} years old.')