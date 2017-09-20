# ball.py
# 볼 송석 설정
# 볼 위치 설정(초기 위치, 다음 이동 위치)
# 속도 설정

from table import *

class Ball:
    def __init__(self, table, width = 24, height=24, color="red", x_speed=10, y_speed=10, x_start=300, y_start=200):
        self.width = width
        self.height = height
        self.x_posn = table.width/2
        self.y_posn = table.height/2
        self.color = color
        self.x_speed = x_speed
        self.y_speed = y_speed

        self.table = table

        self.circle = self.table.draw_oval(self)

    def move_next(self):
        self.x_posn = self.x_posn + self.x_speed
        self.y_posn = self.y_posn + self.y_speed

        if self.x_posn >= self.table.width-3-self.width:
            self.x_posn = self.table.width-3-self.width 
            self.x_speed = -self.x_speed

        if self.x_posn <= 0+3:
            self.x_posn = 0+3
            self.x_speed = -self.x_speed

        if self.y_posn >= self.table.height-3 - self.height :
            self.y_posn = self.table.height-3 - self.height
            self.y_speed = -self.y_speed

        if self.y_posn <= 0+3:
            self.y_posn = 0+3
            self.y_speed = -self.y_speed

        x1 = self.x_posn
        y1 = self.y_posn
        x2 = x1 + self.width
        y2 = y1 + self.height

        self.table.move_item(self.circle, x1, y1, x2, y2)
