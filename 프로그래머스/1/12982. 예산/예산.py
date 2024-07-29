def solution(d, budget):
    team = 0
    d.sort()
    for i in d:
        budget -= i
        if budget >= 0:
            team += 1
        else:
            break
    return team