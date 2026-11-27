a = {1,2,3,4,5,5,5,5,5,6,7} # this will create a set with elements 1,2,3,4,5,6,7
b = {10,11,3,2,5} # this will create a set with elements 10,11,3,2,5

print(a) # this will print the set a
print(b) # this will print the set b
print(a.union(b)) # this will print the union of sets a and b
print(a.intersection(b)) # this will print the intersection of sets a and b
a.remove(2) # this will remove the element 2 from the set a
print(a) # this will print the updated set a
a.add(2) # this will add the element 2 to the set a
print(a) # this will print the set a