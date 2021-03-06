# 장민수
# 컴퓨터 공학과
# 201331040

# myNumber.py
# 함수를 직접 만들어 써봅시다.
import random

# 난이도를 골라봅시다.
print("난이도는 e(쉬움), m(중간), h(어려움)으로 구성되어 있습니다.")
level=input("난이도를 선택해주세요.(쉬움은'e', 중간은 'm', 어려움은 'h'를 눌러주세요.)")

# 사용자가 적절한 난이도를 고를 때까지 반복합니다.
while level != "e" and level !="m" and level!="h":
    print("존재하지 않는 난이도입니다. 난이도를 다시 선택해주세요.")
    level=input("쉬움은'e', 중간은 'm', 어려움은'h'을 눌러주세요.(e/m/h) :")

# 최대 한계값 걸러내기
if(level == "e"):
    max=10
elif(level == "m"):
    max=20
else:
    max=100

# 숫자를 골라봅시다.
computer_number = random.randint(1, max)
count=0

#is_same() 함수를 만듭니다.
def is_same(target, number):
    if number<1 or number>max:
        result ="Out"
    elif target == number:
        result = "Win"
    elif target > number:
        result = "Low"
    else:
        result = "High"
    return result

# 게임을 시작합니다.
print("\n안녕하세요! 숫자 맞추기 게임 진행자입니다.\n저는 1 ~",max,"중 숫자 하나를 골랐어요.")

# 사용자가 추측한 숫자를 인수로 받아옵니다.
guess = int(input("숫자를 쓰고 엔터 키를 누르세요."))
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
print("\n정답!\n잘했어요.",count,"번에 맞추셨네요")
input("\n\n마치려면 엔터 키를 누르세요.")

