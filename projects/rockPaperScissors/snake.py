# Snake in python :0
import msvcrt
import os
import time
import random
from keyboard import is_pressed



screen = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","\n",
          " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","\n",
          " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","\n",
          " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","\n",
          " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","\n",
          " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","\n",
          " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","\n",
          " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","\n",
          " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","\n",
          " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","\n",]

head = 10
tail = 9


input = "a"
while(True):

    screen[head] = "O"
    screen[tail] = " "


    if input == "w":
        tail = head
        if head > 21:
            tail = head
            head -= 21
        else:
            tail = head
            head += 189


    if input == "a":
        tail = head
        head -= 1
        if (screen[head] == "\n") or (head < 0):
            head += 20
            

    if input == "s":
        tail = head
        head += 21
        if head > 210:
            head -= 210
 
    if input == "d":
        tail = head
        head += 1
        if screen[head] == "\n":
            head -= 20
    os.system('cls')
    print("Next Screen")
    if is_pressed("d"):
        input = "d"
    elif is_pressed("s"):
        input = ("s")
    elif is_pressed("a"):
        input = "a"
    elif is_pressed("w"):
        input = "w"

    for i in screen:
        print(i, end="")
    time.sleep(0.5)
