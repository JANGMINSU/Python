# main.py
# 게임 규칙, 테이블 생성, 움직임 제어

from tkinter import *
from table import *

w = Tk()
w.title("MyPong")

table = Table(w)

w.mainloop()
