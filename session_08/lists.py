#!/usr/bin/env python3

'''
Lists are basically the same thing as tuples but they can be manipulated
Lists are ordered sequences represented by square brackets
Lists can have strings, floats, integers, other lists, and other data types
You can make a list of data frames
'''

# Make a list
list1 = ["Viki", "Oran", "Julia", "Kelly", "Felisa"]
print(list1)

# Include multiple data types in a list
list2 = ["Lamp", 3, 7.2, True, (1, 2, 3)]
print(list2)

# Index a list
print(list2[0])
print(list2[0][0])
print(list2[-1])
print(list2[4][1])

# Slice list
cars = ("bmx","audi","toyota","subaru")
some_cars = cars[0:2]
print(some_cars)

# Appending to a list (adding one more object)
my_fav_artists = ["Michael Jackson", "Metallica", "Guns N Roses"]
my_fav_artists.append("Billy Idol")
print(my_fav_artists)
#Notice how the function is after the variable

# Extending a list (if you are adding more than one object)
my_fav_artists.extend(["Journey", "Bon Jovi", "Duran Duran", "Depeche Mode"])
print(my_fav_artists)

# Change list element
my_fav_artists[0] = "Billy Joel"
print(my_fav_artists)

# Delete element
del(my_fav_artists[0])
print(my_fav_artists)

# Remove last item in list
my_fav_artists_popped = my_fav_artists.pop() #removes the last on the list but without really creating another object
print(my_fav_artists)

# Access popped value
print(my_fav_artists_popped)

my_nums = [1, 2, 3, 4, 5]

print(my_nums)
print(*my_nums)
# using * makes the list come our without the list formatting

my_str = "Jack and Jill went up the hill"
split_str = my_str.split()
print(split_str)

# Split using delimiter
alph = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
split_alph = alph.split(",")
print(split_alph)
#if you want to use split by something else rather than a space,
# you include it in the function

# Alias a list
listA = [1, 2, 3, 4, 5]
listB = listA
print(f'List A is originally {listA} and List B is originally {listB}')
# Add an element to listA but don't explicitly change listB
listA.append(6)
print(f'We changed List A and now it is {listA}. Since List B reflects this change as an aliased list, List B is also {listB}.')
#With this you have to be very careful of where your variables are and what you
#are naming them

# Clone a list
listC = listA[:]

# Change listA again but not listC
listA.append(7)
print(listA)
print(listC)
#listC did not change because you cloned it and not aliased it


# Perform simple statistics
listD = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Find the minimum in the list
print(min(listD))
# Find the maximum in the list
print(max(listD))
# Find the sum of the list
print(sum(listD))

print("for-loops can be applied to lists, remember this for the future")
