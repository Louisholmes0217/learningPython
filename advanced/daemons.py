# This runs in the background, usually not important
# program will not wait for these tasks to complete before
# exiting. Non-daemon threads can not normally be killed.

# usecases are getting input, garbage collection, long running
# counters.

import time
import threading
def timer():
    print()
    count = 0
    while True:
        time.sleep(2)
        count += 1 
        print("logged in for: ", count, "seconds")

x = threading.Thread(target=timer, args=(), daemon=True) # Daemon tag means this process will end if the main program ends
x.start()

answer = input("do you wish to quit?\n")
