def solution(polynomial):
    result = [0, 0]
    for i in polynomial.split():
        if i == 'x':
            result[0] += 1
        elif 'x' in i:
            result[0] += int(i[:-1])
        elif i.isdigit():
            result[1] += int(i)
    
    answer = ''
    if result[0]:
        if result[0] == 1:
            answer += 'x'
        else:
            answer += str(result[0]) + 'x'
    
    if result[1]:
        if answer:
            answer += f" + {str(result[1])}"
        else:
            answer += str(result[1])
        
    return answer