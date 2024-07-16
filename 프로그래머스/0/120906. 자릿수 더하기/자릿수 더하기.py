def solution(n):
    result = 0
    for i in sorted(str(n)):
        result += int(i)
    return result