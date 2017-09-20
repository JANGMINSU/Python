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

        else:
            self.canvas.create_line(0, self.height/2, self.width, self.height/2, fill=net_color, dash=(15,23), width=2)


    def draw_oval(self, oval):
        x1=oval.x_posn
        y1=oval.y_posn
        x2=x1+oval.width
        y2=y1+oval.height

        c = self.canvas.create_oval(x1, y1, x2, y2, fill=oval.color)
        return c
    
    def draw_rectangle(self, rec):
        x1=rec.x_posn
        y1=rec.y_posn
        x2=x1+rec.width
        y2=y1+rec.height

        r = self.canvas.create_rectangle(x1, y1, x2, y2, fill=rec.color)
        return r

    def move_item(self, item, x1, y1, x2, y2):
        self.canvas.coords(item, x1, y1, x2, y2)
