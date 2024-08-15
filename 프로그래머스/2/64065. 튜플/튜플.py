def solution(s):
    result = {}
    temp = ''
    
    for x in s:
        if x.isdigit():
            temp += x
        else:
            if temp:
                if temp in result:
                    result[temp] += 1
                elif temp:
                    result[temp] = 1
            temp = ''
            
    return [int(i) for i in sorted(result, key=lambda x: result[x], reverse=True)]