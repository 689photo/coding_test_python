def solution(n):
    lst = '124'
    answer = ''
    
    while n > 0:
        n -= 1
        n, m = divmod(n, 3)
        answer = lst[m] + answer
    
    return answer