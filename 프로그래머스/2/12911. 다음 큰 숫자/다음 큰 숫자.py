def solution(n):
    temp = n + 1
    while str(bin(n)[2:]).count('1') != str(bin(temp)[2:]).count('1'):
        temp += 1
    return temp