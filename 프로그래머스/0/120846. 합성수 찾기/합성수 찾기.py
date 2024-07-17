def solution(n):
    result = 0
    for i in range(1, n+1):
        num = 0
        for x in range(1, i+1):
            if i % x == 0:
                num += 1
                if num > 2:
                    result += 1
                    break
    return result