def solution(arr):
    temp = 0
    result = 0
    while True:
        if temp == len(arr):
            return result - 1
        else:
            temp = 0
            for i in range(len(arr)):
                if arr[i] >= 50 and arr[i] % 2 == 0:
                    arr[i] //=2
                elif arr[i] < 50 and arr[i] % 2 == 1:
                    arr[i] = arr[i] * 2 + 1
                else:
                    temp += 1
        result += 1
    return result