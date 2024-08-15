from itertools import permutations

def solution(k, dungeons):
    result = 0
    
    for i in permutations(dungeons):
        temp = k
        count = 0
        for a in i:
            if temp >= a[0]:
                count += 1
                temp -= a[1]
            else:
                break
        
        if count > result:
            result = count
    
    return result