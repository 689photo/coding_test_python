def solution(s):
    zero = 0
    two = 0
    while int(s) > 1:
        zero += s.count("0")
        s = format(s.count('1'), 'b')
        two += 1
    return [two, zero]