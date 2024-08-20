from itertools import combinations

def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        for a in range(2, int(sum(i) ** 0.5) + 1):
            if sum(i) % a == 0:
                break
        else:
            answer += 1
            
    return answer