import heapq
def solution(operations):
    result = []
    for i in operations:
        if i.startswith('I'):
            heapq.heappush(result, int(i[2:]))
        else:
            if '-1' in i:
                try:
                    heapq.heappop(result)
                except:
                    continue
            else:
                try:
                    result.pop()
                except:
                    continue
                    
    if result == []:
        return [0,0]
    
    return [max(result), min(result)]