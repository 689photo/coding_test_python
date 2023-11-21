def solution(order):
    
    stack = []
    count = 0
    
    for box in range(1, len(order) + 1):
        stack.append(box)
        
        while stack and stack[-1] == order[count]:
            count += 1
            stack.pop()
            
    return count