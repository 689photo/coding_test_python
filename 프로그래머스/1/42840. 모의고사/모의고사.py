def solution(answers):
    result = [0, 0, 0]

    fir = [1, 2, 3, 4, 5]
    sec = [2, 1, 2, 3, 2, 4, 2, 5]
    thd = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for a, e in enumerate(answers):
        if e == fir[a % 5]:
            result[0] += 1
        if e == sec[a % 8]:
            result[1] += 1
        if e == thd[a % 10]:
            result[2] += 1
            
    return [a + 1 for a, e in enumerate(result) if e == max(result)]