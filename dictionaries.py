# a modifiable list of key:value pairs
# extremely fast

capitals = {"USA" : "Washington DC",
            "India" : "New Dehli",
            "China" : "Beijing",
            "Russia" : "Moscow"}

# getting capital of Russia
print(capitals["Russia"])

# safe way of checking if a key value is within a dict, as no error is thrown if not
print(capitals.get("Germany"))

# printing keys in a dict
print(capitals.keys())

# printing values in a dict
print(capitals.values())

# printing all items in a dict
print(capitals.items())

# printing all pairs in a dict
for key,value in capitals.items():
    print(key, value)

# adding keypair to dict
capitals.update({"Germany" : "Berlin"})

# Modifying a value in dict
capitals.update({"USA" : "Las Vegas"})

# remove keypair from dict
capitals.pop("China")

# clear all keypairs in a dict
capitals.clear()