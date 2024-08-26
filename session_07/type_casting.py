#!/usr/bin/env python3

# Assign numbers as an integer, float, and string
a = 1
b = 1.5
c = '1'

# Demonstrate type incompatibilities
print(a + b)
print("the above did not give me an error?")

print(a, type(a))
print(b, type(b))
# trying again to get error code
a2 = 100
b2 = 50.1
print(a2 + b2)

# Store float in d
d = 1.9
print(d, type(d))

# Convert float from d to integer and store that in e
e = int(d)
print(e, type(e))

#Be careful when you convert from float to integer, you could be losing important
#information because Python just cuts off anything after the decimal without rounding

# Functions for type casting

# Turn the string "3" into an integer
my_int = int("3")
print(my_int, type(my_int))

# Turn the number 53 into a string
my_str = str(53)
print(my_str, type(my_str))

# Turn the integer 7 into a float
my_float = float(7)
print(my_float, type(my_float))

'''
Type casting refers to changing the original type that python assigns into
something else.
type casting functions include:
int() data -> integer
str() data -> string
float() data -> float
'''

'''
Important functions to know for math operations
x / y	quotient of x and y
x // y	floored quotient of x and y
x % y	remainder of x/y
-x	x negated
+x	x unchanged

complex(re, im)	a complex number with real part re, imaginary part im (defaults to 0)
c.conjugate()	conjugate to the complex number c
divmod(x, y)	the pair (x // y, x % y)
pow(x, y)	x to the power y
x ** y	x to the power y
'''

#Save
