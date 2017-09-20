from tkinter import *

def click():
    value = entry.get(0.0, END)
    text.delete(0.0, END)
    text.insert(END ,value)

window =Tk()
window.title("My Glossary")

label1 = Label(window, text="입력 값")
label1.grid(row=0, column=0, columnspan=2, sticky=W)

entry = Text(window, width=20, height=1)
entry.grid(row=1, column=0, sticky=W)

button =  Button(window, text="계산", command=click)
button.grid(row=1, column=1, sticky=E)

label2 = Label(window, text="결과")
label2.grid(row=2, column=0, columnspan=2, sticky=W)

text= Text(window, width=40, height=8)
text.grid(row=3, column=0, columnspan=2, sticky=W)

window.mainloop();
