from itertools import permutations
def solution(k, dungeons):
    result = []
    comb = list(permutations(dungeons, len(dungeons)))
    for x in comb:
        num = k
        answer = 0
        for y in x:
            if y[0] > num:
                break
            else:
                num -= y[1]
                answer += 1
        result.append(answer)
    return max(result)