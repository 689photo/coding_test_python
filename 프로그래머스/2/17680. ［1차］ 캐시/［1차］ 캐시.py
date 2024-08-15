def solution(cacheSize, cities):
    cache = []
    answer = 0
    
    for i in cities:
        i = i.lower()
        if i not in cache:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(i)
            else:
                cache.append(i)
                cache.pop(0)
        else:
            answer += 1
            cache.append(cache.pop(cache.index(i)))
    
    return answer