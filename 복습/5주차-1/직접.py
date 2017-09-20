from tkinter import *

can_width = 600
can_height = 400
can_color = "black"

p1_x = can_width / 2
p1_y = can_height / 2
line_width = 5
line_length = 5

def p1_move_N(event):
    global p1_y
    can.create_line(p1_x,p1_y,p1_x,p1_y-line_length, fill = "green", width = line_width)
    p1_y=p1_y-line_length

def p1_move_S(event):
    global p1_y
    can.create_line(p1_x,p1_y,p1_x,p1_y+line_length, fill = "green", width = line_width)
    p1_y=p1_y+line_length

def p1_move_W(event):
    global p1_x
    can.create_line(p1_x,p1_y,p1_x-line_length,p1_y, fill = "green", width = line_width)
    p1_x=p1_x-line_length

def p1_move_E(event):
    global p1_x
    can.create_line(p1_x,p1_y,p1_x+line_length,p1_y, fill = "green", width = line_width)
    p1_x=p1_x+line_length

def erase_all(event):
    can.delete(ALL)

window = Tk()
window.title("마마무")
can = Canvas(width = can_width, height = can_height, bg = can_color, highlightthickness=0)
can.pack()

window.bind("<Up>", p1_move_N)
window.bind("<Down>", p1_move_S)
window.bind("<Left>", p1_move_W)
window.bind("<Right>", p1_move_E)
window.bind("c",erase_all)

window.mainloop()
