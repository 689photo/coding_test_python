from collections import Counter
def solution(k, tangerine):
    cnt = list(Counter(tangerine).items())
    cnt.sort(key=lambda x:x[1], reverse=True)
    answer = 0
    
    for i in cnt:
        k -= i[1]
        answer += 1
        if k <= 0:
            break
    
    return answer