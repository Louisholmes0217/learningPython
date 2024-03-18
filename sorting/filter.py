# filter creates a collection of elements from an itterable when a condition is met

friends = [("Rachel", 19),
           ("Monica", 18),
           ("Pheobe", 17), 
           ("Joey", 16),
           ("Chandler", 12)]

age = lambda data:data[1]>=18 # checks data and returns true if second element of data is >= 18

drinking_buddies = list(filter(age, friends))   # filter returns collection of elements when condition is met, type cast to list

for i in drinking_buddies:
    print(i)