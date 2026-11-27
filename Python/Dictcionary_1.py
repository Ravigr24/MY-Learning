my_dictionary = {"x":1,"y":2,"z":3,"demo":{"a":1,"b":2,"c":3}} # this will create a dictionary with keys x,y,z and values 1,2,3

my_dictionary["x"] = 4 # this will add a new key-value pair to the dictionary with key x and value 4

#my_dictionary.pop("z") # this will remove the key-value pair with key z from the dictionary

print(my_dictionary) # this will print the dictionary
print(my_dictionary.keys()) # this will print the keys of the dictionary 

print(my_dictionary.values()) # this will print the values of the dictionary
print(my_dictionary.items()) # this will print the key-value pairs of the dictionary

print(my_dictionary["demo"]) # this will print the nested dictionary demo
print(my_dictionary["demo"]["b"]) # this will print the value of the key b in the nested dictionary demo