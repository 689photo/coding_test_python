def solution(triangle):
    for line in range(1, len(triangle)):
        for idx in range(len(triangle[line])):
            if idx == 0:
                triangle[line][idx] += triangle[line-1][idx]
            elif idx == len(triangle[line]) - 1:
                triangle[line][idx] += triangle[line-1][-1]
            else:
                triangle[line][idx] += max(triangle[line-1][idx-1], triangle[line-1][idx])
    return max(triangle[-1])