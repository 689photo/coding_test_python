def solution(picture, k):
    result = []
    for x in picture:
        temp = ''
        for y in x:
            temp += y * k
        
        for z in range(k):
            result.append(temp)
    
    return result