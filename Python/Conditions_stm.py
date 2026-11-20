'''IF ELSE STATEMENT'''

x = 110


if(x==10):
    print("X is equal to 10")
elif(x>10):
    print("X is to big")
    if((x>100) & (x<200)):
        print("X is between 100 and 200")
    else:
        print("X is greater than 200")
else:
    print("X is less than 10")


'''LOOPs Condition statement'''

tbl_list = ["Customer", "Product", "Order", "Employee"]

for i in tbl_list:
    if(i.lower() == "order"):
        continue
    print(i)    


for i in tbl_list:
    if(i.lower() == "order"):
        print("Table name is Order")
    else:
        print("Table name is not Order")

for i in tbl_list:
    print(i)
    for x in i:
        print(x)


for i in tbl_list:
    if(i.lower() == "order"):
        break
    print(i) 


'''WHILE LOOP'''

x = 1

while(x<11):
    print(x)
    x = x+1
