def solution(n, words):
    result = [words[0]]
    
    for i in range(1, len(words)):
        if words[i] in result:
            return [(i % n) + 1, (i // n) + 1]
        elif result[-1][-1] != words[i][0]:
            return [(i % n) + 1, (i // n) + 1]
        else:
            result.append(words[i])
            
    return [0, 0]