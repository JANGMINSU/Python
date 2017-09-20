from table import *

class Bat:
    def __init__(self, table, width=15, height=100, x_posn=50, y_posn=50, color="green", x_speed=23, y_speed=23):
        self.width = width
        self.height = height
        self.x_posn = x_posn
        self.y_posn = y_posn
        self.color = color
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.table = table
        self.rectangle = self.table.draw_rectangle(self)

    def move_up(self, event):
        self.y_posn = self.y_posn - self.y_speed
        if self.y_posn <= 0:
            self.y_posn = 0
        x1 = self.x_posn
        y1 = self.y_posn
        x2 = self.x_posn + self.width
        y2 = self.y_posn + self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2)

    def move_down(self, event):
        self.y_posn = self.y_posn + self.y_speed
        if self.y_posn >= self.table.height - self.height:
            self.y_posn = self.table.height - self.height
        x1 = self.x_posn
        y1 = self.y_posn
        x2 = self.x_posn + self.width
        y2 = self.y_posn + self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2)
