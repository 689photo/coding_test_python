def solution(q, r, code):
    result = ''
    for i in enumerate(code):
        if i[0] % q == r:
            result += i[1]
    return result