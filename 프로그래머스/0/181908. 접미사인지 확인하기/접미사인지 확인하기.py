def solution(my_string, is_suffix):    
    if is_suffix == my_string:
        return 1
    elif my_string[- len(is_suffix):] == is_suffix:
        return 1
    return 0