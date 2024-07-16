def solution(a, b):
    ab = int(str(a) + str(b))
    ba = 2 * a * b
    
    if ab >= ba:
        return ab
    return ba