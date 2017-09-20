# 이 클래스는 Table의 처리 공간을 2D 직사각형으로 정의합니다.

from tkinter import *

class Table:
    def __init__(self, window, width=600, height=400, color="black", net_color="green", vertical_net=False, horizontal_net=False):
        self.color = color
        self.width = width
        self.height = height

        self.canvas = Canvas(window, bg=self.color, width=self.width, height = self.height)
        self.canvas.pack()

        if(vertical_net):
            self.canvas.create_line(self.width/2, 0, self.width/2, self.height, width=2, fill=net_color, dash=(15,23))
        if(horizontal_net):
            self.canvas.create_line(0, self.height/2, self.width, self.height/2, width=2, fill=net_color, dash=(15,23))
