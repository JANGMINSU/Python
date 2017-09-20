# myCalculator_expt1.py

from tkinter import *
from decimal import *

### 키 입력 함수
def click(key):
    if key=='=':
        try:
            result = str(eval(display.get()))[0:10]
            display.insert(END,"="+result)
        except:
            display.insert(END, "--> 오류")
    
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
    button = Button(num_pad, text = btn_text ,width=5, command=cmd)
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
    button = Button(num_pad, text = btn_text ,width=5, command=cmd)
    button.grid(row=r, column=c, sticky=E)

    c=c+1
    if c>1:
        c=0
        r=r+1
    

window.mainloop()
