# An attemt to make a terminal based dungeon crawler as a
# learning excercise. This is the main program

screen = [
    [" "] * 100,
    [" "] * 100,
    [" "] * 100,
    [" "] * 100,
    [" "] * 100,
    [" "] * 100,
    [" "] * 100,
    [" "] * 100,
    [" "] * 100,
    [" "] * 100,
    [" "] * 100,
    [" "] * 100,
    [" "] * 100
]
def show_screen():
    for x in screen:
        for y in x:
            print(y,end="")
        print("\n")

class player_model:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
   

player = player_model(5,5)
screen[player.pos_x][player.pos_y] = "O"

show_screen()