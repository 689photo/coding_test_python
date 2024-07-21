def solution(num_list):
    result = 0
    
    for i in num_list:
        temp = 0
        while i > 1:
            temp += 1
            if i % 2 == 0:
                i //= 2
            else:
                i = (i - 1) // 2
        result += temp
    return result