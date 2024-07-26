def solution(s):
    s = s.split()
    s = sorted(list(map(int, s)))
    return f"{s[0]} {s[-1]}"