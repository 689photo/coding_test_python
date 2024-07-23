from math import factorial

def combination_count(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def solution(balls, share):
    return combination_count(balls, share)