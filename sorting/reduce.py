# reduce() applies a function to an itterable and combines them, until only one item remains
import functools

letters = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x, y: x+y, letters) # reduce applies function to first two elements of a list and combines
                                                   # therefore we give 2 parameters to the lambda function, and combine them
print(word)


factorial = [5, 4, 3, 2, 1]

result = functools.reduce(lambda x, y: x*y, factorial)
print(result)