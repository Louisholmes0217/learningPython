# run multiple processes at the same time on different CPU cores. This is different 
# to multithreading
from multiprocessing import Process, cpu_count
import time
time_start=(time.perf_counter())
print(cpu_count())

def counter(num):
    count = 0
    while count < num:
        count +=1

def main():
    a = Process(target=counter, args=(50000000,))
    b = Process(target=counter, args=(50000000,))
    a.start()
    b.start()

    a.join()
    b.join()

    print("finished in:", time.perf_counter()-time_start, "seconds")

if __name__ == "__main__":
    main()