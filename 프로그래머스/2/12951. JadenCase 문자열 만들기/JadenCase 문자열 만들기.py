def solution(s):
    result = ''
    for i in list(s):
        if not result:
            result += i.upper()
        elif result[-1] == ' ':
            result += i.upper()
        else:
            result += i.lower()
    return result