def my_funct(p_x):

    try:
        if(p_x % 2 == 0):
            return 1
    except Exception as e:
        return e

    finally:
        print("Hello world")


res = my_funct(4)
print(res)



## global and local variables

x = 100

def glb_funct():

    x = 5 
    print(x)



glb_funct()