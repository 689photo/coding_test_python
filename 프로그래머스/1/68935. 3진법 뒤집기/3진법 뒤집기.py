def solution(n):
    three = ""
    
    while n > 0:
        n, mod = divmod(n, 3)
        three += str(mod)
        
    return int(three, 3)
