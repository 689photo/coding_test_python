def solution(my_string, indices):
    result = ""
    for x, y in enumerate(my_string):
        if x not in indices:
            result += y
    return result