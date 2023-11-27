from collections import deque
def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    f_sum = sum(queue1)
    s_sum = sum(queue2)
    lim = len(queue1) * 3
    answer = 0
    
    while f_sum != s_sum:
        if f_sum < s_sum:
            queue1.append(queue2.popleft())
            f_sum += queue1[-1]
            s_sum -= queue1[-1]
            answer += 1
        else:
            queue2.append(queue1.popleft())
            f_sum -= queue2[-1]
            s_sum += queue2[-1]
            answer += 1
            
        if answer > lim:
            return -1
        
    return answer