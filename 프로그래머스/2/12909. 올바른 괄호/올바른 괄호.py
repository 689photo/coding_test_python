def solution(s):
    result = ''
    for i in s:
        if i == '(':
            result += i
        else:
            if result and result[-1] == '(':
                result = result[:-1]
            else:
                return False
    if result:
        return False
    return True