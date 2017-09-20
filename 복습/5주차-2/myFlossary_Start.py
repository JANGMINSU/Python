# myFlossary_Start.py

from tkinter import *

# 키 입력 함수:
def click():
    entered_text = entry.get()  # 텍스트 엔트리 위젯으로부터 입력한 텍스트를 문자열 수집
    keys = my_Glossary.keys()

    # keys = list(my_Glossary.keys())
    # keys[3]
    text.delete(0.0, END)
    
    if entered_text in keys:
        text.insert(0.0, my_Glossary[entered_text])
 
    
#### 메인:
window = Tk()
window.title("ABC")

# 레이블 생성
label1 = Label(window, text="정의되어 있는 단어를 입력하고 엔터 키를 누르세요 : ")
label1.grid(row=0, column=0, sticky=W)

# 텍스트 엔트리 위젯 생성
entry = Entry(window, width=20, bg = "light green")
entry.grid(row=1, column =0, sticky=W)

# 제출 버튼 추가
button = Button(window, text="제출", width=5, command=click)
button.grid(row=2, column=0, sticky=W)

# 다른 레이블 생성
label2 = Label(window, text="\n정의")
label2.grid(row=3, column=0, columnspan=2, sticky=W)
# 텍스트 박스 생성
text = Text(window, width = 75, height =6, bg = "light green", wrap=WORD)
text.grid(row=4, column=0, columnspan=2, sticky=W)
# 사전
my_Glossary= {
    '알고리즘':'컴퓨터로 작업을 수행하기 위해 컴퓨터가 이해할 수 있도록 단계별로 설명해놓은 것',
    '버그':'프로그램이 적절하게 동작하는데 실패하거나 또는 전혀 동작하지 않는 원인을 제공하는 코드 조각',
    '2진수':'2진법으로 나타낸 숫자',
    '함수':'재사용할 수 있는 코드 조각'
    }

#### 메인 반복문 실행
window.mainloop()
