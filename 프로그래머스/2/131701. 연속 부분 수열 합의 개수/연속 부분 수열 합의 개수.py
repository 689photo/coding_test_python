def solution(elements):
    twice = elements * 2
    result = []
    for i in range(1, len(elements) + 1):
        for x in range(len(elements)):
            result.append(sum(twice[x:x+i]))
    
    return len(set(result))