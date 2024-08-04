def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    x, y = 1, 2
    
    for i in range(3, n+1):
        x, y = y, (x + y) % 1234567
        
    return y