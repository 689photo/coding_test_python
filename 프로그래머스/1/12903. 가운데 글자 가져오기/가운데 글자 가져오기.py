def solution(s):
    leng = len(s)
    if leng % 2 == 0:
        return s[leng//2 - 1 : leng//2 + 1]
    return s[leng//2]