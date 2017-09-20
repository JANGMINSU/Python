from tkinter import *

canvas_width = 600
canvas_height = 400
canvas_colour = "white"

p1_x = canvas_width / 2
p1_y = canvas_height
line_width=50
line_length=10

def p1_move_N(event):
        global p1_y
        canvas.create_line(p1_x, p1_y, p1_x,(p1_y-line_length), fill = "green", width=line_width)
        p1_y=p1_y-line_length

def p1_move_S(event):
        global p1_y
        canvas.create_line(p1_x, p1_y, p1_x,(p1_y+line_length), fill = "red", width=line_width)
        p1_y=p1_y+line_length

def p1_move_W(event):
        global p1_x
        canvas.create_line(p1_x, p1_y, (p1_x-line_length),p1_y, fill = "blue", width=line_width)
        p1_x=p1_x-line_length

def p1_move_E(event):
        global p1_x
        canvas.create_line(p1_x, p1_y, (p1_x+line_length),p1_y, fill = "pink", width=line_width)
        p1_x=p1_x+line_length

def erase_all(evnet):
    canvas.delete(ALL)
    
window= Tk();
window.title("유락마락")

canvas = Canvas(width = canvas_width, height = canvas_height, bg = canvas_colour, highlightthickness=0)
canvas.pack()

window.bind("<Up>",p1_move_N())
window.bind("<Down>",p1_move_S)
window.bind("<Left>",p1_move_W)
window.bind("<Right>",p1_move_E)
window.bind("u", erase_all)

window.mainloop()
