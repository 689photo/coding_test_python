def solution(emergency):
    rank = sorted(emergency, reverse=True)
    result = {}
    for x, y in enumerate(rank):
        result[y] = x + 1
        
    return [result[i] for i in emergency]