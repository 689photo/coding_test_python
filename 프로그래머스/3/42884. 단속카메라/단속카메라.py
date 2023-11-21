from collections import deque
def solution(routes):
    routes.sort()
    stack = deque()
    stack.append(routes[0])
    answer = 0
    
    for i in range(1, len(routes)):
        print(stack, answer)
        car = stack.pop()
        if car[1] >= routes[i][0]:
            stack.append([routes[i][0], min(car[1], routes[i][1])])
        else:
            answer += 1
            stack.append(routes[i])
        
    return answer + 1