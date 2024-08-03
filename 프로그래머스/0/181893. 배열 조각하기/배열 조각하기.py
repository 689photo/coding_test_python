def solution(arr, query):
    for x, y in enumerate(query):
        if x % 2 == 0:
            arr = arr[:y+1]
        else:
            arr = arr[y:]
    return arr