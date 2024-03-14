# operators are symbols that perform an action to their operands. The combination of operands and
# operators is known as an expression, and an expression returns a value. for example, "+" is an 
# operator, "5" is an operand, and "5 + 5" is an expression that returns 10 as the result.

# arithmetic operators (These take 2 operands and return the result)
a = 5+5     # returns 10 (addition)
b = 10 - 5  # returns 5 (subtraction)
c = 5 * 5   # returns 25 (multiplication)
d = 10 / 2  # returns 5 (division)
e = 25 % 3  # returns 1 (modulo, get the remainder from division)
f = 5 ** 2  # returns 25, (to the power of)
g = 15 // 2 # returns 7, (division rounded down)

# assignment operators (These take 2 operands, the first is the variable and second is a value)
h = 0    # assigns a value to a variable
h += 2   # is the same as h = h + 2 (increments by a given number)
h -= 1   # is the same as h = h - 1 (decrements by a given number)
h *= 10  # is the same as h = h * 10 (multiplies by a given number)
# All in all, any other arithmetic or bitwise operator followed by a number can precede an "=" to modify
# a variable in the same way

# comparison operators (These take 2 operands and returns True or False as a boolean)
i = (10 < 20) # returns True (is less than)
j = (10 > 20) # returns False (is more than)
k = (11 <= 11) # returns True (less than or equal to)
l = (11 >= 11) # returns True (more than or equal to)
m = (10 == 10) # returns True (equal to)
n = (10 != 10) # returns False (NOT equal to)

# logical operators, these combine multiple comparison expressions into a single expression and returns 
# True or False
o = ((10 == 10) and (5 < 3)) # returns False (both expressions have to return true)
p = ((10 == 10) or (5 < 3))   # returns True (if either expressions return true)
q = (not(10 == 10))          # returns false (reverses the result of a boolean expression)

# bitwise operators, these take operands and perform bit level operations raw values (Google these to learn more)
r = 233 & 244    # returns 224 (bitwise AND)
s = 223 | 224    # returns 244 (bitwise OR)
t = 223 ^ 224    # returns 63 (bitwise XOR)
u = ~223         # returns -224 (inverts all bits)
v = 255 << 2     # returns 1024 (bitshift left)
w = 255 >> 2     # returns 63 (bitshift right)


# A few more operator types exist, see https://www.w3schools.com/python/python_operators.asp
# for more