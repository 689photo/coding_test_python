def solution(arr, n):
    for i in range(0, len(arr)):
        if i % 2 == 0 and len(arr) % 2 == 1:
            arr[i] = arr[i] + n
        elif i % 2 == 1 and len(arr) % 2 == 0:
            arr[i] = arr[i] + n
    return arr