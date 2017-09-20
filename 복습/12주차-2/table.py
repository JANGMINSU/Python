from tkinter import *

class Table:
    def __init__(self, win, color="black", net_color="green", width=600, height=400, vertical_net=True):
        self.width = width
        self.height = height
        self.color = color

        self.canvas = Canvas(win, bg=color, width=self.width, height=self.height)

        self.canvas.pack()
        if vertical_net == True:
            self.canvas.create_line(self.width/2, 0, self.width/2, self.height, fill=net_color, dash=(15,23), width=2)
            #window에는 dash 작동안하지만 안에 비우지 말 것!
