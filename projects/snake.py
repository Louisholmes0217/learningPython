# Snake in python :0
import msvcrt
import os
import time
import random
from keyboard import is_pressed
import threading
import msvcrt

input = "d"

def get_input():
    while True:
        key_press = msvcrt.getch()
        if key_press != "":
            
            


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

x = threading.Thread(target=get_input, args=(), daemon=True)

x.start()
while(True):
    
    if "X" not in screen:
        fruit = random.randint(0,20)
        fruit = fruit * random.randint(0,10)
        screen[fruit] = "X"


    if screen[head] != "X":
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

    for i in screen:
        print(i, end="")
    time.sleep(0.5)
