# sets are collections of values that are unordered and unindexed with no duplicate values
# these are far faster than lists in very specific circumstances 

utensils = {"fork", "spoon", "knife"}

# adding item to a set
utensils.add("napkin")

# removing item from set
utensils.remove("spoon")

# removing all items from set
utensils.clear()

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# adding one set to another set
#dishes.update(utensils)
#print(dishes)


# combining 2 sets into a single new set
dinner_table = utensils.union(dishes)

for i in dinner_table:
    print(i)

# comparing similarities between two sets
dishes.add("knife")
print(utensils.difference(dishes))