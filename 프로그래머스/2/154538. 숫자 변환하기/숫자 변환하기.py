from collections import deque
def solution(x, y, n):
    que = deque([[y, 0]])
    
    while que:
        num, idx = que.popleft()
        if num == x:
            return idx

        else:
            if num % 3 == 0 and num // 3 >= x:
                que.append([num // 3, idx + 1])
                #if (num % x) % 3 == 0 and num // 3 >= x:
                    
            if num % 2 == 0 and num // 2 >= x:
                que.append([num // 2, idx + 1])
                #if (num % x) % 2 == 0 and num // 2 >= x:
                    
            if num - n >= x:
                que.append([num - n, idx + 1])

    return -1