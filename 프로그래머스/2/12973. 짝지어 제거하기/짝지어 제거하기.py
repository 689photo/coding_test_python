def solution(s):
    answer = []
    
    for alp in s:
        answer.append(alp)
        if len(answer) > 1 and answer[-1] == answer[-2]:
            answer.pop()
            answer.pop()
    
    return int(answer == [])