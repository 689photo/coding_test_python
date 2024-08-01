def solution(a, b):
    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            a //= i
            b //= i
    
    while b > 1:
        if b % 2 == 0:
            b //= 2
        elif b % 5 == 0:
            b //= 5
        else:
            break
    
    if b == 1:
        return 1
    return 2