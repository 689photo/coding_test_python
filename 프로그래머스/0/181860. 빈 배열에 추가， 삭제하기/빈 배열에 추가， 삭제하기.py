def solution(arr, flag):
    result = []
    for x, y in zip(arr, flag):
        if y:
            result += [x] * x * 2
        else:
            for i in range(x):
                result.pop()
    return result