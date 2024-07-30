def solution(n):
    result = 0
    temp = []
    for i in range(1, n + 1):
        temp.append(i)
        if sum(temp) > n:
            while sum(temp) > n:
                temp.pop(0)
        if sum(temp) == n:
            result += 1
    return result