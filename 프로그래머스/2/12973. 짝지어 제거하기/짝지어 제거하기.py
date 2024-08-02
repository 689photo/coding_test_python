def solution(s):
    result = []
    for i in s:
        if result and result[-1] == i:
            result.pop()
            while len(result) >= 2 and result[-2] == result[-1]:
                result.pop()
                result.pop()
        else:
             result.append(i)   
    
    if result:
        return 0
    return 1