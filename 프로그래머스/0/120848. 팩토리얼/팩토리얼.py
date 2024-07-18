def solution(n):
    num = 1
    result = 1
    
    while result < n:
        num += 1
        result *= num
        
    if result == n:
        return num
    return num - 1