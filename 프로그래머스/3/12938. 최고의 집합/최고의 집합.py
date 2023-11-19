def solution(n, s):
    result = []
    
    if s <= n:
        return [-1]
    
    for i in range(n, 0, -1):
        result.append(s // i)
        s -= result[-1]
    
    return result