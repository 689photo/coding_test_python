def solution(k, m, score):
    score.sort(reverse=True)
    return sum([m * i for i in score[m-1::m]])