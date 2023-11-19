def solution(n, k):
    result = ''
    answer = 0
    
    while n > 0:
        n, mod = divmod(n, k)
        result += str(mod)
    
    result = result[::-1]
    result = result.split('0')
    result = list(i for i in result if i and i != '1')
    
    for x in result:
        for y in range(2, int(int(x)**0.5) + 1):
            if int(x) % y == 0:
                break
        else:
            answer += 1
    
    return answer
    