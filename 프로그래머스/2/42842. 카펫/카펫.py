def solution(brown, yellow):
    tt = brown + yellow
    result = []
    
    for i in range(3, int(tt ** 0.5) + 1):
        if tt % i == 0 and brown == (i - 2) * 2 + (tt//i) * 2:
            result.append(tt // i)
            result.append(i)
    
    return result