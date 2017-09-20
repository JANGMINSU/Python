# MyPong의 주된 파이을 만듭니다.

from tkinter import *
import table, ball

# x축과 y축의 속
x_velocity = 10
y_velocity = 10

window = Tk()
window.title("MyPong")

my_table = table.Table(window, vertical_net=True)

my_ball = ball.Ball(table=my_table, x_speed=x_velocity, y_speed=y_velocity, width=24, height=24, color="red", x_start=228, y_start=188)

###함수
def game_flow():
    my_ball.move_next()
    window.after(50, game_flow)

game_flow()

window.mainloop()
