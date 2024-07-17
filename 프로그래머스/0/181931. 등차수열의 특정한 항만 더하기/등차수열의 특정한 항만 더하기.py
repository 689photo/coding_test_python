def solution(a, d, included):
    number = range(a, a + 1 + (len(included) - 1) * d, d)
    answer = 0
    for i in enumerate(included):
        if i[1]:
            answer += number[i[0]]
    return answer