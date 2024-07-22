def solution(price, money, count):
    result = 0
    num = 0
    
    while num < count:
        num += 1
        result += (price * num)
    
    if result < money:
        return 0
    return result - money