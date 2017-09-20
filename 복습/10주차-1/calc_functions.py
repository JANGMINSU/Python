def factorial(n):
   try:
      if "=" in n:
         n=n[n.index("=")+1:]
      if (eval(n) - int(eval(n))) !=0:
         return "실수값은 팩토리얼을 계산할 수 없습니다."
      n =eval(n)
   except:
      return "값이 잘못되었습니다."
   if n<0:
      return "음수는 팩토리얼을 계산할 수 없습니다."
   if n==0:
      return str(1)
   if n>32:
      return "자리수가 너무 큽니다."
   ans = n
   while n > 1:
      n = n - 1
      ans = ans * n
   return str(ans)

def to_roman(n):
    return "-> roman"

def to_binary(n):
   n=eval(n)
   ans=""
   while n > 1:
      r = n % 2
      ans = str(r)+ ans
      n= n // 2
   ans = "1"+ ans
   return ans

def from_binary(n):
    return "binary - > 10"
