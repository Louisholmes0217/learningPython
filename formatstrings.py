# a better way of constructing complex strings

animal = "cow"
item = "moon"

#print("The "+animal+" jumped over the "+item)

# the format fields insert at every {} in order left to right
print("the {} jumped over the {}".format(animal, item))


# you can choose what index from the format fields go where within the {}
print("the {1} jumped over the {0}".format(animal, item))

# to be more direct, use keyword arguments
print("the {animal} jumped over the {item}".format(animal="Lion", item="Beancan"))

# keyword arguments allow you to reuse certain values in the string
print("the {animal} jumped over the {animal}".format(animal="Lion", item="Lion"))


# to be more efficient you can pre-define a string within a variable, and then call the format() method later
text = ("The {} jumped over the {}")
text.format("grandma", "spaceship")

# adding string padding, 10 chars after the name is inserted
name = ("Awesome")
print("Hello, my name is {:10} :)".format(name))


# adding string padding, 10 chars after the name is inserted
name = ("Awesome")
print("Hello, my name is {:10} :)".format(name))

# right allign the value within the padding
print("Hello, my name is {:>10} :)".format(name))

# left allign the value within the padding
print("Hello, my name is {:<10} :)".format(name))

# center the value in the padding
print("Hello, my name is {:^10} :)".format(name))


# formating numbers in a string
# This will round the number and print only the first 3 decimal places of the float
number = 3.14259
print("The number pi is {:.3f}".format(number))

# print commas into every 1000th position
number = 10000000000000
print("The number is {:,}".format(number))

# print number in various formats
number = 230
print("The number is {:b}".format(number))      # binary
print("The number is {:o}".format(number))      # octal
print("The number is {:x}".format(number))      # hex lower
print("The number is {:X}".format(number))      # hex upper
print("The number is {:E}".format(number))      # scientific notation