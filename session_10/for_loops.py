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

print("I left off on Nested For-Loops")
