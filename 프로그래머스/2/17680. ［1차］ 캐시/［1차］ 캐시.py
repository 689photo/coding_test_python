def solution(cacheSize, cities):
    result = []
    answer = 0
    cities = list(i.upper() for i in cities)
    for i in cities:
        if len(result) < cacheSize and i not in result:
            result.append(i)
            answer += 5            
        elif len(result) > 0 and i not in result:
            result.pop(0)
            result.append(i)
            answer += 5
        elif i not in result:
            answer += 5
        else:
            result.remove(i)
            result.append(i)
            answer += 1
    return answer