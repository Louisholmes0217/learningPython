# single line functions, take many inputs but only take a single expression
# returns that single expression

def double(x):
    return x*2

print(double(5))





# same function in lambda
double = lambda x:x*2
multiply = lambda x, y:x*y
add = lambda x, y, z: x+y+z

print(double(6))
print(multiply(5,6))
print(add(5,6,7))

# age check with lambda
age_check = lambda age: age>18
print(age_check(18))