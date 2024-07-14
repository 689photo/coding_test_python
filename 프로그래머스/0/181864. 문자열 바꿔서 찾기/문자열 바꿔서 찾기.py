def solution(myString, pat):
    result = ''
    for i in pat:
        if i == 'A':
            result += 'B'
        else:
            result += 'A'
    
    return int(result in myString)