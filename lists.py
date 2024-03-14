# lists in python group variables into an itterable

food = ["pizza", "burger", "hotdog", "pasta", "cake"]

# printing entire list
print(food)

# printing first element in list
print(food[0])

# modifying list at index 3
food[2] = "sushi"
print(food)

# printing all items in a list
for i in food:
    print(i)

# adding to a list
food.append("dohnut")
print(food)

# removing from a list
food.remove("pasta")
print(food)

# inserting an item in a list
food.insert(2, "beans")
print(food)

# removing last item from a list
food.pop()
print(food)

# sorting alphabetically
food.sort()
print(food)

# emptying a list
food.clear()
print(food)