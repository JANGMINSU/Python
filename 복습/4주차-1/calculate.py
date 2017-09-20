def calculate(a,b,c):
    if b=='+':
        return a+c
    elif b=='-':
        return a-c
    elif b=='*':
        return a*c
    elif b=='/':
        return a/c
    else:
        print("잘못된 문자를 입력하셨습니다.")
        return
