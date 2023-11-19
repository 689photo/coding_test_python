def solution(n, left, right):
    
    result = []
    
    for i in range(left, right+1):
        temp = divmod(i, n)
        if temp[1] > temp[0]:
            result.append(temp[1] + 1)
        else:
            result.append(temp[0] + 1)
    
    return result
    
    """
    y행의 y까지는 y + 1
    y행의 y부터는 x + 1        
    
    [1, 2, 3]
    [2, 2, 3]
    [3, 3, 3]
    
    00 01 02 03
    1  2  3  4
    
    10 11 12 13
    2  2  3  4
    
    20 21 22 23
    3  3  3  4
    
    30 31 32 33
    4  4  4  4    
    """
    