from math import gcd
def solution(arr):
    num = 1
    result = arr[0]
    
    for i in range(len(arr)-1):
        num = 1
        num *= gcd(result, arr[i+1])
        result = ((result * arr[i+1]) // num)
    return result