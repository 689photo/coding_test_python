def solution(n):
    x = 1
    y = 2
    answer = 2
    
    while answer < n:
        x += y
        answer += 1
        if answer == n:
            return x % 1000000007
        y += x
        answer += 1
        if answer == n:
            return y % 1000000007