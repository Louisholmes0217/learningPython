# walrus operator :=
# only in python 3.8 and up
# assigns variables as part of a larger expression

#happy = True
#print(happy)

print(happy := True)

foods = []
#while True:
#    food = input("What is your favourite food?\n")
#    if food == "quit":
#        break
#    else:
#        foods.append(input)
# can be translated as
while (food := input("What is your favourite food?\n")) != "quit":
    foods.append(food)

for i in foods:
    print(i)