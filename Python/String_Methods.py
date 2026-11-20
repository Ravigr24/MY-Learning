x = "Ravikiran"

print(x.capitalize()) # Capitalizes the first character of the string

print(x.replace('v','b')) # Replaces all occurrences of 'v' with 'b'
print(x.replace('b','v')) # Replaces all occurrences of 'b' with 'v'
print(x.replace('vi','v')) # Replaces 'vi' with 'v'

f = "Raw_data.csv"

if(f.endswith('.csv')):
    print("This is a CSV file")
else:
    print("This is not a CSV file")

if(f.startswith('Raw')):
    print("This is a Raw file")
else:
    print("This is not a Raw file")

s = "Ravikiran GR Babu"

my_list = s.split(' ') # Splits the string into a list of words based on the space character

print(my_list) # Prints the list of words


statement = "Hello Ravikiran. What are you doing today? Hey Ravikiran, I'm Talking to you."

print(statement.count('Ravikiran')) # Counts the number of occurrences of 'Ravikiran' in the string
print(statement.count('ar')) # Counts the number of occurrences of 'ar' in the string


demo_str = "Hello"

demo_var = "10abc"

print(demo_str.isnumeric()) # Checks if the string is numeric
print(demo_var.isnumeric()) # Checks if the variable is numeric
print(demo_var.isalnum()) # Checks if the variable is alphanumeric

