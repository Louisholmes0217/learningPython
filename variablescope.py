# the scope of a variable is where that variable is recognizable by the program
# a variable is only reachable within the region where it was created

# creating variable in the main program
name = "MyName"

# creating a variable within a function
def print_name():
    name2 = "MyName2"
    # printing within the function
    print(name2)

print(name)

# This throws an error
#print(name2)