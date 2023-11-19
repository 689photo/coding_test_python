from heapq import heapify, heappush, heappop

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    works = [-1 * i for i in works]
    heapify(works)
    print(works)
    
    while n:
        heappush(works, heappop(works) + 1)
        n -= 1
        
    return sum([i ** 2 for i in works])