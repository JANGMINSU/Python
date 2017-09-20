# Graphic User Interface
from tkinter import *

# 변수 설정
canvas_height = 400
canvas_width = 600
canvas_colour = "white"

# 메인
window = Tk()
window.title("장민수님의 그림판")
canvas = Canvas(bg=canvas_colour, height=canvas_height, width=canvas_width)
canvas.create_line(0,0,600,400, fill="green", width=5)
canvas.create_line(600,0,0,400, fill="green", width=5)
canvas.pack()

window.mainloop()
