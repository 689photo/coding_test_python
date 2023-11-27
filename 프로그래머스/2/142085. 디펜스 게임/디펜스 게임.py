import heapq as hq
def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    
    heap = enemy[:k]
    hq.heapify(heap)
    
    for i in range(k, len(enemy)):
        n -= hq.heappushpop(heap, enemy[i])
        if n < 0:
            return i
    return len(enemy)