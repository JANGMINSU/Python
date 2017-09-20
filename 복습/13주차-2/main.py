# main.py
# 게임 규칙, 테이블 생성, 움직임 제어

from tkinter import *
from table import *
from ball import *

w = Tk()
w.title("MyPong")

my_table = Table(w)
my_ball = Ball(my_table)

def game_flow():
    my_ball.move_next()
    w.after(50, game_flow)

game_flow()

w.mainloop()
