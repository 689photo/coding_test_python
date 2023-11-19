from collections import deque
def solution(maps):
    
    max_x = len(maps[0]) - 1
    max_y = len(maps) - 1
    
    que = deque([[0, 0, 1]])
    move_x = [0, 0, 1, -1]
    move_y = [1, -1, 0, 0]
    
    while que:
        y, x, idx = que.popleft()
        maps[y][x] = 0
        
        if y == max_y and x == max_x:
            return idx
        
        for i in range(4):
            next_x = x + move_x[i]
            next_y = y + move_y[i]
            if 0 <= next_x <= max_x and 0 <= next_y <= max_y and maps[next_y][next_x] == 1:
                que.append([next_y, next_x, idx + 1])
                maps[next_y][next_x] = 0

    return -1