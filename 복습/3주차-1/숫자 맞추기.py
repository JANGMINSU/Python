# myNumber.py
# 함수를 직접 만들어 써봅시다.
import random

# 숫자를 골라봅시다.
computer_number = random.randint(1,100)


#is_same() 함수를 만듭니다.
def is_same(target, number):
    if number<1 or number>100:
        result ="Out"
    elif target == number:
        result = "Win"
    elif target > number:
        result = "Low"
    else:
        result = "High"
    return result
# 추측 count 변수 선언
count=0
# 게임을 시작합니다.
print("안녕.\n난 1부터 100 중 숫자 하나를 골랐어요.")

# 사용자가 추측한 숫자를 인수로 받아옵니다.
guess = int(input("뭔지 쓰고 엔터 키를 누르세요."))
count=count+1

# is_same() 함수를 사용합니다.
higher_or_lower = is_same(computer_number, guess)

# 사용자가 맞출 때까지 게임을 합니다.
while higher_or_lower !="Win":
    if higher_or_lower == "Out":
        guess = int(input("범위를 벗어난 값입니다. 다시 입력하세요. "))
    elif higher_or_lower == "Low":
        guess = int(input("그것보단 높습니다. 다시 생각해보세요. "))
    else:
        guess = int(input("그것보단 낮습니다. 다시 생각해보세요. "))
        
    count=count+1
    higher_or_lower = is_same(computer_number, guess)

# 게임을 끝냅니다.
print("정답!잘했어요.",count,"만에 맞추셨네요.")
input("\n\n마치려면 엔터 키를 누르세요.")

