def solution(m, n, puddles):
    
    #한 줄
    if m == 1 or n == 1:
        if len(puddles[0]) > 0:
            return 0
        return 1
    
    #지도
    mapping = [[0 for _ in range(m)]for __ in range(n)]
    mapping[0][0] = 1

    #웅덩이
    if len(puddles[0]) > 0:
        for i in puddles:
            mapping[i[1] - 1][i[0] - 1] = -1
    
    for y in range(n):
        for x in range(m):
            if y == 0 and x == 0:
                continue
            elif mapping[y][x] == -1:
                mapping[y][x] = 0
            elif y == 0:
                mapping[y][x] = mapping[y][x - 1]
            elif x == 0:
                mapping[y][x] = mapping[y - 1][x]
            else:
                mapping[y][x] += mapping[y][x - 1] + mapping[y - 1][x]


    return mapping[n-1][m-1] % 1000000007