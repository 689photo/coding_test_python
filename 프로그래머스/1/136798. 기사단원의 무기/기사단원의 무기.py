def solution(number, limit, power):
    
    result = []
    
    for i in range(1, number + 1):
        temp = 0
        for a in range(1, int(i ** 0.5) + 1):
            if i % a == 0:
                temp += 2
                if i // a == i ** 0.5:
                    temp -= 1
        
        if temp > limit:
            result.append(power)
        
        else:
            result.append(temp)
        
    return sum(result)