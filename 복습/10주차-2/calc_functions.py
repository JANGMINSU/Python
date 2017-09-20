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

   # n = (eval)n
   
   numberBreaks = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
   
   letters = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL",10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
   result = ""
   
   for b in numberBreaks:
         d = n // b
         while d > 0:
               result = result+letters[b]
               d = d - 1
         n = n % b
      
   return result

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
