def solution(quiz):
    result = []
    for i in quiz:
        eq = i.index('=')
        if eval(i[:eq]) == int(i[eq + 2:]):
            result.append('O')
        else:
            result.append('X')
    return result