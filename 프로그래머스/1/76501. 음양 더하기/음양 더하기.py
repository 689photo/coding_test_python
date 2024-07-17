def solution(absolutes, signs):
    answer = 0
    for i in enumerate(signs):
        if i[1]:
            answer += absolutes[i[0]]
        else:
            answer -= absolutes[i[0]]
    return answer