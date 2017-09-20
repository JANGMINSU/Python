from tkinter import *
from random import *

def click1():
    questions=list(my_dic.keys())
    entry.delete(0, END)
    output.delete(0.0, END)
    
    entry.insert(END, questions[randint(0,3)])

def click2():
    quest=entry.get()
    output.delete(0.0, END)
    output.insert(END, my_dic[quest])

window = Tk()
window.title("IDEA 1")

button1 = Button(window, text="질문 얻기", command=click1)
button1.grid(row=0, column=0, sticky=W)

button2 = Button(window, text="답 얻기", command=click2)
button2.grid(row=0, column=1, sticky=E)

entry = Entry(window, width=20, bg="light green")
entry.grid(row=1, column=0, sticky=W)

label1 = Label(window, text="\n정의")
label1.grid(row=2, column=0, sticky=W)

output = Text(window, width=80, height=10, wrap=WORD, bg="light green")
output.grid(row=3, column=0, columnspan=2, sticky=W)

my_dic={
    '알고리즘':'컴퓨터로 작업을 수행하기 위해 컴퓨터가 이해라 수 있도록 단계별로 설명해놓은 것',
    '버그':'프로그램이 적절하게 동작하는데 실패하거나 또는 전혀 동작하지 않는 원인을 제공하는 코드 조각',
    '2진수':'2진법으로 나타낸 숫자',
    '대화형 모드':'IDLE(Python IDE-통합개발환경)을 벗어나 코드를 저장하지 않고 테스트하고자 할 때 사용합니다.'
    }

window.mainloop()
