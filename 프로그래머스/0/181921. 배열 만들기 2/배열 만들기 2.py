from itertools import product

def solution(l, r):
    
    zf = [0,5]
    number = [int(''.join(map(str, i))) for i in product(zf, repeat=len(str(r)))]
    number = [i for i in number if l <= i <= r]
    
    if number:
        return number
    return [-1]