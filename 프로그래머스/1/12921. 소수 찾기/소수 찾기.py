def solution(n):
    result = 0
    for i in range(2, n+1):
        for a in range(2, int(i ** 0.5) + 1):
            if i % a == 0:
                break
        else:
            result += 1
            
    return result