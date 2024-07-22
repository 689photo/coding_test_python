def solution(n):
    result = []
    i = 2
    
    while i <= n:
        if n % i == 0:
            if i not in result:
                result.append(i)
            n = n // i
        else:
            i += 1
    return result