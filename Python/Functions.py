def my_fun(p_x):
    if( p_x >= 10):
        print("The value is greater than or equal to 10 and the value is: ", p_x)
    else:
        print("The value is not greater than or equal to 10 and the value is: ", p_x)

    return p_x

my_fun(15) 
my_fun(5)
my_fun(10)
my_fun(20)

returned_value = my_fun(25)

print("The returned value is: ", returned_value)