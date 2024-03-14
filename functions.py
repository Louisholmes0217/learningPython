# functions perform a task and return a result when called
# this stopps repeating code and keeps things organized

# defining a function
def helloFunc():
    print("Hello")

# calling function
helloFunc()


# function with parameters
def funcWithParams(param1):
    print(param1)

# calling function and passing argument
funcWithParams("This is my argument")

# function that returns result
def funcWithReturn():
    return 5

print(funcWithReturn())

# useful example
def findArea(radius):
    pi = 3.142
    area = pi * (radius **2)
    return area

circle_rad = 55
circle_area = findArea(circle_rad)
print("circle area for radius", circle_rad, "=", circle_area)