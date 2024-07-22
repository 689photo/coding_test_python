def solution(order):
    menu = {'americano' : 4500, 'latte' : 5000, 'any' : 4500}
    result = 0
    
    for i in menu.keys():
        for drink in order:
            if i in drink:
                result += menu[i]
    return result