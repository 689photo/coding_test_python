from math import gcd

def solution(arr):
    result = 1
    
    for i in arr:
        result = abs(result * i) // gcd(result, i)
    
    return result