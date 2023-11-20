from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    
    que = deque([[begin, 0]])
    answer = 0
    
    while que:
        word, count = list(que.popleft())
        if word == target:
            return count
        count += 1
        for v in words:
            lst = list(v)
            temp = 0
            for i in range(len(lst)):
                if lst[i] != word[i]:
                    temp += 1
            if temp == 1:
                que.append([v, count])

    return 0