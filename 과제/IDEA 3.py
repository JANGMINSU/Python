# main.py
# 게임 규칙, 테이블 생성, 움직임 제어

from tkinter import *
from table import *
from ball import *
from bat import *

w = Tk()
w.title("MyPong")

my_table = Table(w, vertical_net=False)
my_ball = Ball(my_table)
bat_down = Bat(my_table, x_posn=250, y_posn=350, width=100, height=15)


stop = False

def game_flow():
    global stop
    my_ball.move_next()
    bat_down.detect_collision(my_ball)

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

w.bind("<Left>", bat_down.move_left)
w.bind("<Right>", bat_down.move_right)

w.mainloop()
