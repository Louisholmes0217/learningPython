import time

# find out computers epoch, when did time begin?
print(time.ctime(0)) # converts a time expressed in seconds since the computers epoch. returns a string

# shows how many seconds have passed since epoch on comuters clock
print(time.time())

# show current data and time
print(time.ctime(time.time()))

