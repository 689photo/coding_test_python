def solution(numbers):
    if numbers[-1] == 0:
        return '0'
        
        
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key = lambda x: (x * 4)[:4], reverse=True)
    
    return ''.join(numbers)