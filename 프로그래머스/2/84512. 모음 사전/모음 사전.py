from itertools import product
def solution(word):
    alp = ['A', 'E', 'I', 'O', 'U']
    dic = []
    
    for x in range(1, 6):
        for y in product(alp, repeat=x):
            dic.append(''.join(y))
    dic.sort()

    return dic.index(word) + 1