def solution(name, yearning, photo):
    dic = dict(zip(name, yearning))
    result = []
    
    for x in photo:
        temp = 0
        for y in x:
            if y in name:
                temp += dic[y]
        result.append(temp)
    
    return result