def solution(babbling):
    baby = ["aya", "ye", "woo", "ma"]
    result = 0
    
    for i in babbling:
        for a in baby:
            if a * 2 in i:
                break
            i = i.replace(a, '0')
        if all(char == '0' for char in i):
            result += 1
    
    return result