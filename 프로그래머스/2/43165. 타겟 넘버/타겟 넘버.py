from collections import deque
def solution(numbers, target):
    l = len(numbers)
    que = deque([])
    que.append([0, 0])
    answer = 0
    
    while que:
        total, idx = que.popleft()
        if idx == l and total == target:
            answer += 1
        elif idx < l:
            que.append([total + numbers[idx], idx + 1])
            que.append([total - numbers[idx], idx + 1])
        
    return answer