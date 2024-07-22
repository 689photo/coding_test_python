def solution(my_string):
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    num = [0] * 52
    
    for i in my_string:
        num[abc.index(i)] += 1
    
    return num