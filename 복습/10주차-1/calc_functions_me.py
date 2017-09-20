def factorial(n):
    try:
        n = int(n)
    except:
        return "--> 오류!"

    if n == 0:
        return 1
    if n > 40:
        return "--> 답이 화면을 가득 채울 수 있습니다!"
    if n < 0:
        return "--> 오류!"
    
    ans = n
    while n > 1:
        n = n - 1
        ans = ans * n
    return str(ans)

def to_roman(n):
    return "-> roman"

def to_binary(n):
    try:
        n = int(n)
        return bin(n)[2:]
    except:
        return "--> 오류!"
    
def from_binary(n):
    try:
        return int(n, 2)
    except:
        return "--> 오류!"
