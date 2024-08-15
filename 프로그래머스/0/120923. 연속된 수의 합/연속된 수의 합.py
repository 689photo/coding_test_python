def solution(num, total):
    ave = total / num
    start = int(ave - (num - 1) / 2)
    return list(range(start, start + num))