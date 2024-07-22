def solution(s):
    result = 0
    s = s.split()
    for i in enumerate(s):
        if i[1] == 'Z':
            result -= int(s[i[0] - 1])
        else:
            result += int(i[1])
    return result