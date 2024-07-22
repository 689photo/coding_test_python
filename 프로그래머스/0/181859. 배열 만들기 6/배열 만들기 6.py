def solution(arr):
    i = 0
    stk = []
    
    while i < len(arr):
        if stk and stk[-1] == arr[i]:
            stk.pop()
            i += 1
        else:
            stk.append(arr[i])
            i += 1
    
    if not stk:
        return [-1]
    return stk