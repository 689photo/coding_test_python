def solution(arr, k):
    def multiple(x):
        return x * k
    
    def plus(y):
        return y + k

    if k % 2 == 1:
        return list(map(multiple, arr))
    else:
        return list(map(plus, arr))