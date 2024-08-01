def solution(n):
    result = []
    temp = 0
    for i in range(1, 101):
        temp += 1
        while temp % 3 == 0 or '3' in str(temp):
            temp += 1
        result.append(temp)
    return result[n-1]