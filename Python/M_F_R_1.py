#map,filter,reduce 

from functools import reduce

my_list = [1,2,3,4,5,6,7,8]

# def square(p_x):

#     ret_list = [i*i for i in p_x]
#     return ret_list

# result = square(my_list)
# print(result)

def square_list(p_x):

    if(p_x %2 == 0):
        return p_x*p_x
    
result_map = list(map(square_list,my_list)) # this will apply the square_list function to each element in the my_list
result_filter = list(filter(square_list,my_list)) # this will filter the elements in the my_list based on the square_list function

print(result_map) # this will print the result of the map function
print(result_filter) # this will print the result of the filter function


def add(p_x,p_y):

    return p_x+p_y

result_reduce = reduce(add,my_list) # this will apply the add function to each element in the my_list
print(result_reduce) # this will print the result of the reduce function