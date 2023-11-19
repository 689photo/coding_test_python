from collections import deque
def solution(priorities, location):
    que = deque([i for i in range(len(priorities))])
    answer = 0
    maxi = max(priorities)
    
    while True:
        index = que.popleft()
        if priorities[index] < maxi:
            que.append(index)
        else:
            answer += 1
            priorities[index] = 0
            maxi = max(priorities)
            if index == location:
                return answer