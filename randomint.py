import random

x = random.randint(1, 6)    # random int
y = random.random()         # random float

mylist = ["rock", "paper", "scissors"]
z = random.choice(mylist)   # random val from list

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)       # shuffle list randomly

print(y)
