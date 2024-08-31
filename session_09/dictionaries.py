#!/usr/bin/env python3

'''
When creating a dictionary, you need to use curly brackets {}
Dictionaries have keys and values
The keys can not be changed (immutable)
The values can be immutable, mutable, and duplicates
Each key and value pair are separated by a comma
'''

# Make our first dictionary
dict1 = {'a':0, 'b':1, 'c':2}
print(dict1)

# Mix data types in a dictionary
dict2 = {"my_string":"Coffee", "my_int": 8, "my_float":9.2, "my_list":[1, 2, 3, 4, 5]}
print(dict2)

# Find values in a dictionary
dict3 = {
  "brand": "Honda",
  "model": "Civic",
  "year": 2020
}
print(dict3["brand"])

# Add new value dictionary entry
dict3["owner"] = "Sadie"
print(dict3)

# Delete dictionary entry
del(dict3["owner"])
print(dict3)

# Check if elements are in the dictionary (note that it only works for keys)
check1 = "owner" in dict3
print(check1)
check2 = "year" in dict3
print(check2)
check3 = 2020 in dict3
print(check3)

# View all keys
print(dict3.keys())
# View all values
print(dict3.values())