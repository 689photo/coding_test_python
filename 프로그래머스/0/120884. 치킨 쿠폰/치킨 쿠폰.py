def solution(chicken): 
    result = 0
    
    while chicken >= 10:
        chicken, ticket = divmod(chicken, 10)
        result += chicken
        chicken += ticket
    
    return result