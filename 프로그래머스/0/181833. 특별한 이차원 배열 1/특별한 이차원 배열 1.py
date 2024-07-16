def solution(n):
    result = [[0 for i in range(n)] for i in range(n)]
    
    for x in range(n):
        for y in range(n):
            if x == y:
                result[x][y] = 1
    
    return result