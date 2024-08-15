from math import ceil

def solution(progresses, speeds):
    progresses = [ceil((100 - a) / e) for a, e in zip(progresses, speeds)]
    
    date = progresses[0]
    deploy = 0
    result = []
    
    for i in progresses:
        if i - date <= 0:
            deploy += 1
        else:
            result.append(deploy)
            deploy = 1
            date = i
    
    result.append(deploy)
    
    return result