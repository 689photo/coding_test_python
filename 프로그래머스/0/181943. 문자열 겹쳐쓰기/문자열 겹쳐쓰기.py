def solution(my_string, overwrite_string, s):
    length = len(my_string) - len(overwrite_string) - s
    if length > 0:
        return my_string[:s] + overwrite_string + my_string[-length:]
    else:
        return my_string[:s] + overwrite_string
