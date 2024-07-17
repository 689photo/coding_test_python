def solution(my_string):
    result = []
    for i in sorted(my_string):
        try:
            result.append(int(i))
        except:
            break
    return result