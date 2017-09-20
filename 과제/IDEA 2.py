# 장민수
# 컴퓨터 공학과
# 201331040

from tkinter import *
from random import *

def click1():
    questions=list(my_dic.keys())
    print(questions)
    entry.delete(0, END)
    output.delete(0.0, END)
    
    entry.insert(END, questions[randint(0,25)])

def click2():
    quest=entry.get()
    output.delete(0.0, END)
    output.insert(END, my_dic[quest])

window = Tk()
window.title("IDEA 1")

button1 = Button(window, text="질문 얻기", command=click1)
button1.grid(row=0, column=0, sticky=W)

button2 = Button(window, text="다음 질문", command=click1)
button2.grid(row=0, column=1, sticky=E)

entry = Entry(window, width=80, bg="light green")
entry.grid(row=1, column=0, columnspan=2, sticky=W)

button3 = Button(window, text="정답 얻기", command=click2)
button3.grid(row=2, column=0, sticky=W)

label1 = Label(window, text="\n정답 : ")
label1.grid(row=3, column=0, sticky=W)

output = Text(window, width=80, height=10, wrap=WORD, bg="light green")
output.grid(row=4, column=0, columnspan=2, sticky=W)

my_dic={
    'apple':'사과',
    'bear':'곰',
    'cat':'고양이',
    'dog':'개',
    'elephant':'코끼리',
    'fish':'물고기',
    'goose':'오리',
    'horse':'말',
    'ice-cream':'아이스크림',
    'juice':'쥬스',
    'key':'열쇠',
    'lion':'사자',
    'mouse':'쥐',
    'nut':'땅콩',
    'orange':'오렌지',
    'pig':'돼지',
    'queen':'여왕',
    'rabbit':'토끼',
    'sun':'태양',
    'tiger':'호랑이',
    'umbrella':'토끼',
    'violine':'바이올',
    'wolf':'늑대',
    'xylophone':'실로폰',
    'yacht':'요트',
    'zebra':'얼룩말'
    }

window.mainloop()
