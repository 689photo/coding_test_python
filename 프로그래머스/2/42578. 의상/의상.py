def solution(clothes):
    lst = {y : [] for x, y in clothes}
    answer = 1
    
    for x, y in clothes:
        lst[y].append(x)
    
    for i in list(lst.values()):
        answer *= len(i) + 1
    
    return answer - 1