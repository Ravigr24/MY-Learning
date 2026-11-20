my_list_2 = [1,2,3,4,5,6]

print(my_list_2[::-1]) # this will print the list in reverse order but it will not reverse the list permanently

my_list_2.reverse() # it will reverse full list permenently
print(my_list_2)

for i in reversed(my_list_2):
    print(i)  # this will not reverse the list permanently, it will just print the list in reverse order


my_list_1 = [1,2,"Ravikiran", "GR",['aa','bb','cc']]
my_list = [1,2,"Ravikiran", "GR", 3,4,5,6]

my_list.append("Hero")
my_list.pop()

my_list.insert(2,"Hero")

print(my_list)
print(my_list[::2])
print(my_list_1[4][1]) 
print(my_list[0:3])
print(my_list[-3:])


