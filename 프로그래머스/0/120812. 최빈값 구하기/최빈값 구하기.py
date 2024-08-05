def solution(array):
    dic = {}
    for i in array:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    if len(dic) >1 and sorted(dic.values())[-1] == sorted(dic.values())[-2]:
        return -1
    return [x for x, y in dic.items() if y == sorted(dic.values())[-1]][0]