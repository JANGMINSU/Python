# 장민수
# 컴퓨터 공학과
# 201331040

def to_roman(n):

   # n = (eval)n

   # 현재 로마자의 표현범위는 0~3999까지 입니다.
   if n>3999:
       return "--> 표현 범위를 넘습니다."
   
   romans = ((1000,"M"), (900,"CM"), (500,"D"), (400,"CD"), (100,"C"), (90,"XC"), (50,"L"), (40,"XL"), (10,"X"), (9,"IX"), (5,"V"), (4,"IV"), (1,"I"))
   result = ""

   for i in romans:
       while(n>=i[0]):
            result = result + i[1]
            n = n - i[0]
            
   return result
