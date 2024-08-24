def solution(n, m, section):
    result = 0
    painted = 0
    for i in section:
        if i <= painted:
            continue
        else:
            painted = i + m - 1
            result += 1
    return result