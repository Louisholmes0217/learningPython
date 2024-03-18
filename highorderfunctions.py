
# you can pass functions as arguments to other functions

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func, text):
    print(func(text))

# passing function as argument to make a string upper
hello(loud, "this is a message")

# passing function as argument to make a string lower
hello(loud, "this is a message")

# you can also return functions from functions
def divisor(x):
    def divident(y):
        return y / x
    
    return divident

divide = divisor(2)
print(divide(10))