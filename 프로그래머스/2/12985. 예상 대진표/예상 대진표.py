from math import ceil
def solution(n,a,b):
    rnd = 0 
    while a != b:
        rnd += 1
        a = ceil(a/2)
        b = ceil(b/2)
    
    return rnd