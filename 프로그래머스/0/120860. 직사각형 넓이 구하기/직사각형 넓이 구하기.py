def solution(dots):
    result = [[], []]
    for x, y in dots:
        result[0].append(x)
        result[1].append(y)
    return (max(result[0]) - min(result[0])) * (max(result[1]) - min(result[1]))
