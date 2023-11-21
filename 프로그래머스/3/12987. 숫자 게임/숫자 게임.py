def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    answer = 0
    stack = []
    stack.append(A.pop())
    
    while B:
        if stack[-1] >= B.pop():
            continue
        else:
            answer += 1
            stack.pop()
            if A == []:
                break
        stack.append(A.pop())
    return answer