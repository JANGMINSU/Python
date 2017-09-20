# main.py
# 게임 규칙, 테이블 생성, 움직임 제어

from tkinter import *
from table import *
from ball import *
from bat import *

w = Tk()
w.title("MyPong")

my_table = Table(w)
my_ball = Ball(my_table)
bat_L = Bat(my_table, x_posn=20, y_posn=150, color="blue")
bat_R = Bat(my_table, x_posn=565, y_posn=150, color="yellow")

stop = False

def game_flow():
    global stop
    my_ball.move_next()
    if stop == True:
        return
    w.after(50, game_flow)

game_flow()

def game_stop(event):
    global stop
    stop = True
    
w.bind("p", game_stop)

def game_restart(event):
    global stop
    if stop==True:
        stop = False
        game_flow()

w.bind("r", game_restart)

w.bind("+", my_ball.speed_up)
w.bind("-", my_ball.speed_down)

w.bind("a", bat_L.move_up)
w.bind("z", bat_L.move_down)
w.bind("<Up>", bat_R.move_up)
w.bind("<Down>", bat_R.move_down)

w.mainloop()
