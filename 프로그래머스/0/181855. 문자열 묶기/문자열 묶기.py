def solution(strArr):
    result = {}
    
    for i in strArr:
        if len(i) in result:
            result[len(i)] += 1
        else:
            result[len(i)] = 1
    
    return sorted(result.values(), reverse=True)[0]