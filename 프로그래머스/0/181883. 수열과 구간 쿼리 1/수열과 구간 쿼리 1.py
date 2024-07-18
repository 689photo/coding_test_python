def solution(arr, queries):
    for i in queries:
        for n in range(i[0], i[1] + 1):
            arr[n] += 1
    return arr