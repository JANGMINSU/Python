from tkinter import *
from calc_functions import *
# import calc_functions

num_pad_list=[
'7', '8', '9',
'4', '5', '6',
'1', '2', '3',
'0', '.', '=']


op_pad_list=[
'*', '/',
'+', '-',
'(', ')',
'C', '']

con_list = [
    'pi',
    '빞의 이동 속도 (m/s)',
    '소리의 이동 속도 (m/s)',
    '태양과의 평균 거리 (km)']

fun_list = [
    'factorial (!)',
    '-> roman',
    '-> binary',
    'binary - > 10']


def click(event):
    key=event.widget["text"]
    if key=='=':
        try:
            result = str(eval(display.get()))[0:10]
            display.insert(END, " = " + result)
        except:
            display.insert(END,"--> 오류")
    elif key=='C':
        display.delete(0, END)
    elif key==con_list[0]:
        display.insert(END, "3.141592654")
    elif key==con_list[1]:
        display.insert(END, "300000000")
    elif key==con_list[2]:
        display.insert(END, "330")
    elif key==con_list[3]:
        display.insert(END, "149597887.5")
    elif key==fun_list[0]:
        n = display.get()
        display.delete(0, END)
        display.insert(END, factorial(n))
    elif key==fun_list[1]:
        n = display.get()
        display.delete(0, END)
        display.insert(END, to_roman(n))
    elif key==fun_list[2]:
        n = display.get()
        display.delete(0, END)
        display.insert(END, to_binary(n))
    elif key==fun_list[3]:
        n = display.get()
        display.delete(0, END)
        display.insert(END, from_binary(n))
    else:
        display.insert(END, key)

w = Tk()
w.title("My calculator")

display = Entry(w, width=45, bg="light green")
display.grid(columnspan=2)

num_pad = Frame(w)
num_pad.grid(row=1, column=0, sticky=W)

r = 0
c = 0

for btn_text in num_pad_list:
    b= Button(num_pad, text=btn_text, width=6)
    b.bind("<Button-1>", click)
    b.grid(row=r, column=c)
    c=c+1
    if c == 3:
        c=0
        r=r+1


op_pad = Frame(w)
op_pad.grid(row=1, column=1, sticky=E)

r = 0
c = 0

for op_text in op_pad_list:
    b= Button(op_pad, text=op_text, width=7)
    b.bind("<Button-1>", click)
    b.grid(row=r, column=c)
    c=c+1
    if c == 2:
        c=0
        r=r+1

con_pad = Frame(w)
con_pad.grid(row=2, column=0, sticky=W)

r=0
c=0

for con_text in con_list:
    b=Button(con_pad, text=con_text, width=21)
    b.grid(row=r, column=c, sticky=W)
    b.bind("<Button-1>", click)
    r=r+1

fun_pad = Frame(w)
fun_pad.grid(row=2, column=1, sticky=E)

r=0
c=0

for fun_text in fun_list:
    b=Button(fun_pad, text=fun_text, width=16)
    b.grid(row=r, column=c, sticky=E)
    b.bind("<Button-1>", click)
    r=r+1

w.mainloop()
