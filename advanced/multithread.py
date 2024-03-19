# thread is a flow of execution
# can run different parts of a program at different times
# they run concurrently but not in parallel.
# they each take a turn running one step of execution and iterate through
# multiprocessing has programs running in true parallel

# in CPU bound processes, multiprocessing is best
# IO bound processing, multithreading is best

import threading # module needed for threads
import time

def eat_breakfast():
    time.sleep(3)
    print("you eat breakfast")

def drink_coffee():
    time.sleep(4)
    print("you drank coffee")

def study():
    time.sleep(5)
    print("you finished studying")


# this runs sequentially. Cannot run functions at the same time
#eat_breakfast()
#drink_coffee()
#study()

# creating a new thread and running them
x = threading.Thread(target=eat_breakfast, args=())
y = threading.Thread(target=drink_coffee, args=())
z = threading.Thread(target=study, args=())
x.start()
y.start()
z.start()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

# waiting for one thread to wait for another thread to finish
x.join()
#y.join()
#z.join()

print("done")