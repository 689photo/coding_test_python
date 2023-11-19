def solution(n):
    m = n
    while True:
        m = m + 1
        if bin(m)[2:].count('1') == bin(n)[2:].count('1'):
               break
    return m