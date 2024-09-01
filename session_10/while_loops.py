#!/usr/bin/env python3

# Basic while-loop with 10 iterations
i = 0
while i < 10:
	print(i)
	i += 1
    
# A while-loop with two variables
x = 11
y = 1
while y < x:
	print(y)
	y += 1
    

'''# Broken while-loop
i = 0
while i < 10:
	print(i)
#To interrupt a broken/never ending loop: ctrl + C
'''



# More complicated while-loop
dates = [1982, 1980, 1973, 2000]
i = 0
year = 0
while year != 1973:
    year = dates[i]
    i = i + 1
    print(year)
print("It took ", i ,"repetitions to get out of loop.")

# Another complicated while-loop
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 1
Rating = PlayListRatings[0]
while Rating >= 6:
    print(Rating)
    Rating = PlayListRatings[i]
    i += 1

# One last while-loop for reference
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while squares[i] == 'orange':
    new_squares.append(squares[i])
    i += 1
print(new_squares)