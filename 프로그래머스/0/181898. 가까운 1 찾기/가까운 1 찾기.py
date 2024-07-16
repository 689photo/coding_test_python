def solution(arr, idx):
    if len(arr) < idx:
        return -1
    
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1