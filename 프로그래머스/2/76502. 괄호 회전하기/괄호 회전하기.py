def solution(s):
    answer = 0
    lst = list(s)
    
    for i in range(len(lst)):
        stack = []
        for x in range(len(lst)):
            if stack:
                if stack[-1] == '[' and lst[x] == ']':
                    stack.pop()
                elif stack[-1] == '{' and lst[x] == '}':
                    stack.pop()
                elif stack[-1] == '(' and lst[x] == ')':
                    stack.pop()
                else:
                    stack.append(lst[x])
            else:
                stack.append(lst[x])
        
        if len(stack) == 0:
            answer += 1
        lst.append(lst.pop(0))
    return answer
    
    
    """
    answer = 0
    lst = list(s)
    
    for i in range(len(s)):
        temp = []
        for x in range(len(lst)):
            if len(temp) > 0:
                if temp[-1] == '[' and lst[x] == ']':
                    temp.pop()
                elif temp[-1] == '(' and lst[x] == ')':
                    temp.pop()
                elif temp[-1] == '{' and lst[x] == '}':
                    temp.pop()
                else:
                    temp.append(lst[x])
            else:
                temp.append(lst[x])
            
        if len(temp) == 0:
            answer += 1
        lst.append(lst.pop(0))
    return answer"""