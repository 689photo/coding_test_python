def solution(brown, yellow):
    by = brown + yellow
    result = []
    for i in range(1, int((by + 1)**0.5) + 1):
        if by % i == 0:
            result.append([by//i, i])
            
    print(result)
    
    for i in result:
        if i[1] <= 2:
            continue
        else:
            if (i[0] - 2) * (i[1] - 2) == yellow:
                return i