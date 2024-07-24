def solution(arr, queries):
    result = []
    
    for s, e, k in queries:
        temp = 1000001
        
        for i in arr[s:e+1]:
            if i > k and i < temp:
                temp = i
        
        if temp == 1000001:
            result.append(-1)
        else:
            result.append(temp)
            
    return result