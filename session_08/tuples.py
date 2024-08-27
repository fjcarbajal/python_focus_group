#!/usr/bin/env python3

tuple1=("disco", 10, 1.2)
print(type(tuple1))

#Tuples are ordered sequences
#they can not be changed
#They can contain strings, integers, and floats

# Indexing tuples
tuple1=("disco",10,1.2)
first_element = tuple1[0]
first_el_type = type(tuple1[0])
first_el_type2 = type(first_element)
print(tuple1[0], type(tuple1[0]))

# We can access the last element by using -1 index
# Using negative indexing
last = tuple1[-1]
second_to_last = tuple1[-2]
third_to_last = tuple1[-3]
print(f'The last element is {last}. The second to last element is {second_to_last}. The third to last (first in this case) element is {third_to_last}')

#index function to find the element index
genres_tuple = ("pop","rock","soul","hard rock","soft rock","R&B","progressive rock","disco")
print(genres_tuple.index("disco"))
print(genres_tuple.index("rock"))

# Slicing tuples
tuple_to_slice = ("disco", 10, 1.2, "hard rock", 10)
print(tuple_to_slice[0:3])
#remember the last index in the code above needs to have the index +1 so its [0:3] not [0:2]
# Determine length of tuple
print(len(tuple_to_slice))

## Sorting Tuples
# Use the sorted() function
Ratings = (10,9,6,5,10,8,9,6,2)
print(f'The original tuple is: {Ratings}')

RatingsSorted = sorted(Ratings)
print(f'The sorted tuple is: {RatingsSorted}. Notice that our original tuple, {Ratings} is still unsorted')
#Notice how the sorted tuple now has [] this signifies that the tuple was transformed into a list
#because they can not be changed, the tuple needed to be transformed in order for us
#to manipulate it
print(type(RatingsSorted))

# Sort tuple with strings
Cars=("bmx","audi","toyota","subaru")
Cars_sorted = sorted(Cars)
print(Cars_sorted)
#they are sorted in alphabetical order

# Concatenating tuples
tuple1 = ("disco", 10, 1.2)
tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)
#if we want to combine tuples - by making a new one

#Nesting refers to a data type containing a sequence data type
# Work with nested tuples
nested_tuple = (1, 2, ("pop", "rock"), (3, 4), ("disco", (5, 6)))

# Access the nested tuple at index 2
print(nested_tuple[2])

# Access the first element of the nested tuple at index 2 ("pop")
print(nested_tuple[2][0])

# Access the double nested 6 at the very end of the tuple
print(nested_tuple[4][1][1])

# Access the "s" in "disco"
print(nested_tuple[4][0][2])
#Go back to Session 6 for review