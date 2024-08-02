def solution(A, B):
    result = ''
    for i in range(len(A)):
        if A[-i:] + A[0:-i] == B:
            return i
    return -1