from tkinter import *

canvas_height = 400
canvas_width = 600
canvas_colour = "black"

p1_x = canvas_width / 2
p1_y = canvas_height

line_length = 5
line_width = 5

def pl_move_N():
    global p1_y
    canvas.create_line(p1_x,p1_y,p1_x,p1_y-line_length, fill="green", width = line_width)
    p1_y = p1_y - line_length

window = Tk()
window.title("MyEtchASketch")

canvas = Canvas(bg=canvas_colour, height = canvas_height, width= canvas_width, highlightthickness=0)

pl_move_N()

canvas.pack()

window.mainloop()
