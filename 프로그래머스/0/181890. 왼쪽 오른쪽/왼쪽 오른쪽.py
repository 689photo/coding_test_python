def solution(str_list):
    if 'l' in str_list and 'r' in str_list:
        lw = str_list.index('l')
        rw = str_list.index('r')
        
        if lw < rw:
            return str_list[:lw]
        else:
            return str_list[rw + 1:]
    
    elif 'l' in str_list:
        return str_list[:str_list.index('l')]
    elif 'r' in str_list:
        return str_list[str_list.index('r') + 1:]
    else:
        return []