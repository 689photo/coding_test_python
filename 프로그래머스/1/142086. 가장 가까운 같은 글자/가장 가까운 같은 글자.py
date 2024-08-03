def solution(s):
    result = []
    answer = []
    for i in s:
        if i in result:
            answer.append(result.index(i) + 1)
        else:
            answer.append(-1)
        result.insert(0, i)
    
    return answer