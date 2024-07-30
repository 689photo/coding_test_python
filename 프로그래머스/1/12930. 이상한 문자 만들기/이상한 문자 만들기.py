def solution(s):
    result = ''
    s = list(s)
    temp = 0
    
    for i in s:
        if result and result[-1] == ' ':
            temp = 0
            result += i.upper()
        else:
            if temp % 2 == 0:
                    result += i.upper()
            else:
                result += i.lower()
        temp += 1
    return result