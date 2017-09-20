from random import *

# 내가 임의로 지정하는 비밀번호
MY_PASSWORD="abcdefg"

response1 = "걱정말고 다시 시도해보세요."
response2 = "그럴 듯하지만 내 비밀번호는 아니예요. 다시 한번 입력해보세요."
response3 = "내 비밀번호가 아니예요. 내 비밀번호는 정말 쉬워요."
response4 = "잘 했습니다."

def is_correct(guess, password):
    if guess == password:
        return True
    else:
        return False

print("안녕\n")
user_guess = input("추측한 비밀번호를 입력하시오.")

true_or_false  = is_correct(user_guess, MY_PASSWORD)

while true_or_false == False:
    computer_response = randint(1, 3)
    if computer_response == 1:
        print(response1)
    elif computer_response == 2:
        print(response2)
    else:
        print(response3)
    user_guess = input("\n 다음 비밀번호는 무엇입니까?")
    true_or_false  = is_correct(user_guess, MY_PASSWORD)

print(response4)
input("\n\n\n엔터키를 눌러 종료하세요.")
