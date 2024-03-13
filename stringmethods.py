import string

str = "This is my string"

# get length, returns int
print(len(str))

# find method, returns int index
print(str.find("s"))

# make uppercase, returns upper case string
print(str.upper())

# make lowercase, returns lower case string
print(str.lower())

# detecting if numeric, returns bool
print(str.isdigit())

# detecting if alpha, returns bool
print(str.isalpha())

# detecting if alphanumeric, returns bool
print(str.isalnum())

# counting characters in string, returns int
print(str.count("i"))

# replacing a character, returns new string
print(str.replace("i", "G"))

# operators also work with strings
print(str*3)