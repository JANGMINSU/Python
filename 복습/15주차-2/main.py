# main.py
# 게임 규칙, 테이블 생성, 움직임 제어

from tkinter import *
from table import *
from ball import *
from bat import *

score_left = 0
score_right = 0

w = Tk()
w.title("MyPong")

my_table = Table(w)
my_ball = Ball(my_table)
bat_L = Bat(my_table, x_posn=20, y_posn=150, color="blue")
bat_R = Bat(my_table, x_posn=565, y_posn=150, color="yellow")

stop = False

def initialize():
        my_ball.stop_ball()
        my_ball.start_position()
        bat_L.start_position()
        bat_R.start_position()
        my_table.move_item(bat_L.rectangle, 20, 150, 35, 250)
        my_table.move_item(bat_R.rectangle, 565, 150, 580, 250)

def game_flow():
    global stop
    global score_left
    global score_right
    my_ball.move_next()
    if my_ball.x_posn <= 3:
        initialize()
        score_right = score_right + 1
        my_table.draw_score(score_left , score_right)
    if my_ball.x_posn >= my_table.width - my_ball.width -  3:
        initialize()
        score_left = score_left + 1
        my_table.draw_score(score_left , score_right)
         
    bat_L.detect_collision(my_ball)
    bat_R.detect_collision(my_ball)
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

def restart_game(event):
        my_ball.start_ball()


w.bind("r", game_restart)

w.bind("+", my_ball.speed_up)
w.bind("-", my_ball.speed_down)

w.bind("a", bat_L.move_up)
w.bind("z", bat_L.move_down)
w.bind("<Up>", bat_R.move_up)
w.bind("<Down>", bat_R.move_down)
w.bind("<space>", restart_game)

w.mainloop()
