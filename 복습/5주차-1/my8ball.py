# MyFortuneCookie

from random import *

# 답변을 입력해 봅시다.
ans=("오늘 하루가 엄청 위험해요!",
     "새로운 동료를 만날거 같네요!",
     "오늘 돈 좀 벌겠는데요?",
     "오늘 하루는 정신 없이 바쁠거 같네요",
     "남을 너무 믿지 마세요! 상처 받을 거 같네요",
     "오늘은 무조건 왼쪽을 선택해주세요",
     "오늘 하루는 일을 쉬는게 좋겠어요",
     "당신은 오늘 하루가 고단할거 같네요")

print("MyFortuneCookie에 오신 것을 환영합니다.")

# 사용자의 질문 얻기
question = input("포츈 쿠키를 뜯으시려면 엔터 키를 누르세요.\n")

print("포츈 쿠키를 깨는 중...\n" * 3)

# 질문에 알맞은 답변을 하는 일에 randint() 함수를 활용합니다.
choice=randint(0, 7)

# 화면에 답변을 출력합니다.
print(ans[choice])

input("\n\n마치려면 엔터 키를 누르세요.")
