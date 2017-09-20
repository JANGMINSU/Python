# MyPong의 주된 파이을 만듭니다.

from tkinter import *
import table, ball, bat

# x축과 y축의 속
x_velocity = 10
y_velocity = 10

window = Tk()
window.title("MyPong")

my_table = table.Table(window, vertical_net=True)

my_ball = ball.Ball(table=my_table, x_speed=x_velocity, y_speed=y_velocity, width=24, height=24, color="red", x_start=300, y_start=200)

bat_L = bat.Bat(table=my_table, width=15, height=100, x_posn=20, y_posn=150, color="blue")
bat_R = bat.Bat(table=my_table, width=15, height=100, x_posn=575, y_posn=150, color="yellow")

###함수
def game_flow():
    my_ball.move_next()
    
    if (my_ball.x_posn <= 3):
        my_ball.stop_ball()
        my_ball.start_position()
        bat_L.start_position()
        bat_R.start_position()
        my_table.move_item(bat_L.rectangle, 20, 150, 35, 250)
        my_table.move_item(bat_R.rectangle, 575, 150, 590, 250)

    if (my_ball.x_posn >= my_table.width - my_ball.width - 3):
        my_ball.stop_ball()
        my_ball.start_position()
        bat_L.start_position()
        bat_R.start_position()
        my_table.move_item(bat_L.rectangle, 20, 150, 35, 250)
        my_table.move_item(bat_R.rectangle, 575, 150, 590, 250)
    
    bat_L.detect_collision(my_ball)
    bat_R.detect_collision(my_ball)
    window.after(50, game_flow)

window.bind("a", bat_L.move_up)
window.bind ("z", bat_L.move_down)
window.bind("<Up>", bat_R.move_up)
window.bind("<Down>", bat_R.move_down)

def restart_game(master):
    my_ball.start_ball(x_speed = x_velocity, y_speed=0)
    
window.bind("<space>", restart_game)

game_flow()

window.mainloop()
