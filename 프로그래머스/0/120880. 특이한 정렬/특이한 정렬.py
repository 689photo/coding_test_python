def solution(numlist, n):
    numlist = sorted(numlist, key=lambda x : (abs(x - n), -x))
    return numlist