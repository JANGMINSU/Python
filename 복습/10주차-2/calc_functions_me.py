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
    try:
        n = int(n)
    except:
        return "-->오류"

    if n > 4999:
        return "--> 범위를 넘어섭니다."

    numberBreaks = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)

    letters = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}

    result = ""
    for i in numberBreaks:
        while n>=i:
            result = result + letters[i]
            n = n - i

    return result

    
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
