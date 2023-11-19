def solution(n, t, m, p):
    answer = '0'
    result = ''
    x = 1

    while len(answer) < (t * m) + p:
        stri = ''
        y = x
        while y > 0:
            y, mod = divmod(y, n)
            if mod == 10:
                mod = 'A'
            elif mod == 11:
                mod = 'B'
            elif mod == 12:
                mod = 'C'
            elif mod == 13:
                mod = 'D'
            elif mod == 14:
                mod = 'E'
            elif mod == 15:
                mod = 'F'
            stri += str(mod)
        answer += stri[::-1]
        x = x + 1
        
    for i in range(p, (m * t) + 1, m):
        result += str(answer[i-1])
    
    return result