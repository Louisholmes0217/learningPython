# *args is a paramater that will pack all passed arguments into a tuple
# useful for adding an unknown amount of arguments to a function
# args doesnt have to be args, it is the "*" that matters. "*stuff" works the same

def add(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(add(4, 5, 6, 3, 2, 34, 4, 3))
print(add(5, 10))