def solution(n):
    result = [0, 1, 1, 2, 3, 5]
    
    for i in range(n):
        result += [result[-1] + result[-2]]
    
    return result[n] % 1234567