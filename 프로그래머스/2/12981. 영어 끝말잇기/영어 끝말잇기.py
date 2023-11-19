def solution(n, words):
    result = []
    oc = []
    for x, y in enumerate(words):
        if y in oc:
                return [(x % n) + 1, (x // n) + 1]
        oc.append(y)
        if len(oc) > 1:
            if oc[-2][-1] != y[0]:
                return [(x % n) + 1, (x // n) + 1]
    else:
        return [0,0]
                