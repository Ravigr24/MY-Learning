x =1

if(x==1):
    print("x is equal to 1")
print("This is outside the if block")


'''Type casting topic'''

a = 10

b = '15'

b_new = int(b)

a_new = str(a)

print(type(b_new))
print(type(a_new))


'''Arrays topic'''

x = "Ravikiran"

print(x[0]) # Accessing the first character of the string
print(x[4]) # Accessing the 5th character of the string
print(x[-1]) # Accessing the last character of the string

print(len(x)) # Getting the length of the string
print(x[0:len(x)]) # Accessing the entire string using slicing

print(x[0:5]) # Accessing characters from index 0 to 4
print(x[2:]) # Accessing characters from index 2 to the end
print(x[:5]) # Accessing characters from the start to index 4
print(x[0:11]) # Accessing characters from index 0 to 10
print(x[3:7]) # Accessing characters from index 3 to 6
