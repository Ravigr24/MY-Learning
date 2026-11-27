my_list = [1,2,3,4,5,6]

new_list =  [i*i for i in my_list if (i % 2) == 0 if(i!=6)] # this will print the square of each element in the list which is even and not equal to 6
#for i in my_list:
#   new_list.append(i*i)

print(new_list) # this will print the square of each element in the list

print(my_list[-3:]) # this will print the last 3 elements of the list
print(my_list[::2]) # this will print the list in alternate order
