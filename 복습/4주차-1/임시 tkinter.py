from tkinter import *

ht = 400
wh = 600
colour = "black"

x1=300
y1=400
col1="green"
linewh=5
linelen=5

def move(event):
    global y1

    canvas.create_line(x1,y1,x1,(y1-linelen),width=linewh,fil=col1)
    y1=y1-linelen


window = Tk()
window.title("그림판")
canvas = Canvas(bg = colour, height = ht, width =wh, highlightthickness=0)
move(1)

canvas.pack()

window.mainloop()
