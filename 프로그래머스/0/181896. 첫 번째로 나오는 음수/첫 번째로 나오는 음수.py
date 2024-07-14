def solution(num_list):
    for i in enumerate(num_list):
        if i[1] < 0:
            return i[0]
    return -1