# MyPong의 주된 파이을 만듭니다.

from tkinter import *
import table

window = Tk()
window.title("MyPong")

my_table = table.Table(window, vertical_net=True, horizontal_net=True)

window.mainloop()
