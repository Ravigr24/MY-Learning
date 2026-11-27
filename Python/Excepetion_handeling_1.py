x = "10"

try:
    if(x>10):
        print("x is greater than 10")
    else:
        print("x is less than or equal to 10")
except Exception as e:
    print("An error occurred:", e)

finally:
    print("I will run always no matter what.")
    
print("Program continues after exception handling.")

