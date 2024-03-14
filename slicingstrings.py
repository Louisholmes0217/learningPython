# slicing a string into a list with delimeter

name = "My name"

# printing using indexes
firstname = name[0:2]
lastname = name[3:9]
print(firstname, lastname)

# indexing with a step counter
funkyname = name[0:9:2]
print(funkyname)

# reversing using indexing, with a step counter of -1
reversedname = name[::-1]
print(reversedname)

# slicing a string with an index and negative index
website = "http://google.com"
slice = slice(7,-4)
print(website[slice])

