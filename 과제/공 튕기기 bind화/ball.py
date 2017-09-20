# ball.py
# 볼 송석 설정
# 볼 위치 설정(초기 위치, 다음 이동 위치)
# 속도 설정

from table import *
from random import *

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
        self.start_ball()

    def start_ball(self):
        if randint(0,1):
            self.x_speed = self.x_speed
        else:
            self.x_speed = -self.x_speed
        if randint(0,1):
            self.y_speed = self.y_speed
        else:
            self.y_speed = -self.y_speed


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

    def stop_next(self, event):
        if(self.x_speed!=0 and self.y_speed!=0):
            self.x_start = self.x_speed
            self.x_speed = 0
            self.y_start = self.y_speed
            self.y_speed = 0

    def start_next(self, event):
        if(self.x_speed==0 and self.y_speed==0):
            self.x_speed = self.x_start
            self.y_speed = self.y_start

    def speed_up(self, event):
        if(self.x_speed>0 and self.x_speed<20):
            self.x_speed += 1
        elif(self.x_speed<0 and self.x_speed>-20):
            self.x_speed += -1
        if(self.y_speed>0 and self.y_speed<20):
            self.y_speed += 1
        elif(self.y_speed<0 and self.y_speed>-20):
            self.y_speed += -1

    def speed_down(self, event):
        if(self.x_speed>1):
            self.x_speed -= 1
        elif(self.x_speed<-1):
            self.x_speed -= -1
        if(self.y_speed>1):
            self.y_speed -= 1
        elif(self.y_speed<-1):
            self.y_speed -= -1
