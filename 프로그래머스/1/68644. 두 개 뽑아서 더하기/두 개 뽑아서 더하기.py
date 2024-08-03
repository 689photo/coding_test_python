from itertools import combinations

def solution(numbers):
    result = []
    for i in combinations(numbers, 2):
        if sum(i) not in result:
            result.append(sum(i))
            
    return sorted(result)