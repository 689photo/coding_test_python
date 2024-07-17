def solution(date1, date2):
    if int(''.join(map(str, date1))) < int(''.join(map(str, date2))):
        return 1
    return 0