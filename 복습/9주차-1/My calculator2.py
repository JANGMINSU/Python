from tkinter import *

w = Tk()
w.title("My calculator")

display = Entry(w, width=45, bg="light green")
display.grid(columnspan=2)

num_pad = Frame(w)
num_pad.grid(row=1, column=0, sticky=W)

num_pad_list=[
'7', '8', '9',
'4', '5', '6',
'1', '2', '3',
'0', '.', '=']

def click(key):
    if key=='=':
        try:
            result = str(eval(display.get()))[0:10]
            display.insert(END, " = " + result)
        except:
            display.insert(END,"--> 오류")
    elif key=='C':
        display.delete(0, END)
    else:
        display.insert(END, key)
r = 0
c = 0

for btn_text in num_pad_list:
    def cmd(k=btn_text):
        click(k)
    b= Button(num_pad, text=btn_text, width=5, command=cmd)
    b.grid(row=r, column=c)
    c=c+1
    if c == 3:
        c=0
        r=r+1


op_pad = Frame(w)
op_pad.grid(row=1, column=1, sticky=E)

op_pad_list=[
'*', '/',
'+', '-',
'(', ')',
'C', '']

r = 0
c = 0

for op_text in op_pad_list:
    def cmd(k=op_text):
        click(k)
    b= Button(op_pad, text=op_text, width=5, command=cmd)
    b.grid(row=r, column=c)
    c=c+1
    if c == 2:
        c=0
        r=r+1
w.mainloop()
