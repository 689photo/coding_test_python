def solution(k, tangerine):
    result = {}
    
    for i in tangerine:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    
    result = sorted(result.values(), reverse = True)
    
    answer = 0
    count = 0
    for i in result:
        answer += i
        count += 1
        if answer >= k:
            return count