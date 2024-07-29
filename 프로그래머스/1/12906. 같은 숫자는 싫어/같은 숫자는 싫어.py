def solution(arr):
    result = [arr[0]]
    for i in arr:
        if result[-1] != i:
            result.append(i)
    return result