def solution(clothes):
    clo = {}
    answer = 1
    
    for i in clothes:
        if i[1] in clo:
            clo[i[1]] += 1
        else:
            clo[i[1]] = 1
    
    
    for i in clo.values():
        answer *= (i + 1)
    
    return answer - 1