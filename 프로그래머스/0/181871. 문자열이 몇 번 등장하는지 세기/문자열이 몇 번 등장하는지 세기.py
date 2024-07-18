def solution(myString, pat):
    return [myString[i:i+len(pat)] for i in range(len(myString)-len(pat)+1)].count(pat)