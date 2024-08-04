import bisect

def solution(k, score):
    ranker = []
    result = []
    
    for i in score:
        bisect.insort(ranker, i)
        if len(ranker) > k:
            ranker = ranker[1:]
        result.append(ranker[0])
    return result