def my_funct(**p_x):

    print(p_x, type(p_x))
    print(p_x['x'], p_x['y'], p_x['z'], p_x['w'])
    print(p_x.keys())
    print(p_x.values())
    print(p_x.get('x'), p_x.get('y'), p_x.get('z'), p_x.get('w'))

my_funct(x=20, y=50, z=60, w=70)




# def addiction(x,y):
#     return x+y

# var = addiction(10,20)
# print("The addition of x and y is: ", var)

var = lambda x,y: x+y
var = var(10,20)
print("The addition of x and y is: ", var)