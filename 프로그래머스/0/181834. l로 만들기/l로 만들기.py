def solution(myString):
    result = ''
    for i in myString:
        if i < 'l':
            result += 'l'
        else:
            result += i
    return result