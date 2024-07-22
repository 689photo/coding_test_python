def solution(arr):
    num = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    temp = 0
    
    for i in num:
        if i >= len(arr):
            temp += i
            break
            
    return arr + [0] * (temp - len(arr))