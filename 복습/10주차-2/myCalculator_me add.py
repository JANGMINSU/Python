# myCalculator_expt1.py

from tkinter import *
from decimal import *
from calc_functions_me import *

### 키 입력 함수
def click(key):
    if key=='=':
        try:
            result = str(eval(display.get()))[0:10]
            display.insert(END,"="+result)
        except:
            display.insert(END, "--> 오류")
    elif key==con_pad_list[0]:
        display.insert(END,"3.141592654")
    elif key==con_pad_list[1]:
        display.insert(END,"300000000")
    elif key==con_pad_list[2]:
        display.insert(END,"330")
    elif key==con_pad_list[3]:
        display.insert(END,"149597887.5")

    elif key==fun_pad_list[0]:
        n = display.get()
        display.delete(0, END)
        display.insert(END, factorial(n))
    elif key==fun_pad_list[1]:
        n = display.get()
        display.delete(0, END)
        display.insert(END, to_roman(n))
    elif key==fun_pad_list[2]:
        n = display.get()
        display.delete(0, END)
        display.insert(END, to_binary(n))
    elif key==fun_pad_list[3]:
        n = display.get()
        display.delete(0, END)
        display.insert(END, from_binary(n))
        
    elif key=='C':
        display.delete(0, END)
    else:
        display.insert(END, key)

### 메인
window=Tk()
window.title("MyCalculator")

top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

display = Entry(top_row, width=45, bg="light green")
display.grid(columnspan=3)

num_pad = Frame(window)
num_pad.grid(row=1, column=0, sticky=W)

num_pad_list = [
    '7','8','9',
    '4','5','6',
    '1','2','3',
    '0','.','=' ]

r=0
c=0

for btn_text in num_pad_list:
    def cmd(x=btn_text):
        click(x)
    button = Button(num_pad, text = btn_text ,width=6, command=cmd)
    button.grid(row=r, column=c, sticky=W)

    c=c+1
    if c>2:
        c=0
        r=r+1

num_pad = Frame(window)
num_pad.grid(row=1, column=1, sticky=E)

op_pad_list = [
    '*','/',
    '+','-',
    '(',')',
    'C','' ]

r=0
c=0

for btn_text in op_pad_list:
    def cmd(x=btn_text):
        click(x)
    button = Button(num_pad, text = btn_text ,width=6, command=cmd)
    button.grid(row=r, column=c, sticky=E)

    c=c+1
    if c>1:
        c=0
        r=r+1

con_pad = Frame(window)
con_pad.grid(row=2, column=0, sticky=W)

con_pad_list = [
    "Pi",
    "빛의 이동 속도 (m/s)",
    "소리의 이동 속도 (m/s)",
    "태양과의 평균 거리(km)" ]

r=0
c=0

for con_text in con_pad_list:
    def cmd(x=con_text):
        click(x)
    button = Button(con_pad, width=21, text=con_text, command=cmd)
    button.grid(row=r, column=c, sticky=W)
    r=r+1

fun_pad = Frame(window)
fun_pad.grid(row=2, column=1, sticky=E)


fun_pad_list = [
    "factorial (!)",
    "-> roman",
    "-> binary",
    "binary - > 10" ]

r=0
c=0
    
for fun_text in fun_pad_list:
    def cmd(x=fun_text):
        click(x)
    button = Button(fun_pad, width=14, text=fun_text, command=cmd)
    button.grid(row=r, column=c, sticky=W)
    r=r+1
    
window.mainloop()
