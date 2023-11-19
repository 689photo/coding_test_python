def solution(s):
    s = s.split(' ')
    print(s)
    return ' '.join(i.capitalize() for i in s)