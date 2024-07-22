def solution(left, right):
    result = 0
    for x in range(left, right + 1):
        temp = 0
        for y in range(1, int(x ** 0.5) + 1):
            if x % y == 0 and y == x ** 0.5:
                temp += 1
        if temp == 1:
            result -= x
        else:
            result += x
    return result