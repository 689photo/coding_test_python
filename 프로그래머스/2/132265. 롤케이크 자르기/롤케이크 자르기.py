from collections import Counter
def solution(topping):
    old = Counter(topping)
    young = set()
    answer = 0
    
    for i in topping:
        young.add(i)
        
        if i in old:
            old[i] -= 1
            if old[i] == 0:
                del old[i]
        
        if len(young) == len(old.keys()):
            answer += 1
            
    return answer