def solution(s):
    answer = 0
    
    if len(s) % 2 == 1:
        return 0
    
    for i in range(len(s)):
        result = []
        v = True
        for a in s[i:] + s[:i]:
            if a in '[{(':
                result.append(a)
            elif a == ']' and (not result or result[-1] != '['):
                v = False
                break
            elif a == '}' and (not result or result[-1] != '{'):
                v = False
                break
            elif a == ')' and (not result or result[-1] != '('):
                v = False
                break
            else:
                result.pop()
        
        if v and not result:
            answer += 1
        
    return answer           