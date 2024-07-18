def solution(my_string):
    result = 0
    temp = ''
    for i in my_string:
        if i.isdigit():
            temp += i
        else:
            if temp:
                result += int(temp)
            temp = ''
    if temp:
        result += int(temp)
    return result