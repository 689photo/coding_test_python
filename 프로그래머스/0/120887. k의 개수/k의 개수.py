def solution(i, j, k):
    result = 0
    for i in range(i, j+1):
        result += str(i).count(str(k))
    return result