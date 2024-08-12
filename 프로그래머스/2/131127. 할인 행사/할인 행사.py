from collections import Counter

def solution(want, number, discount):
    want_dict = dict(zip(want, number))
    
    n = len(discount)
    window_size = 10
    result = 0
    
    for i in range(n - window_size + 1):
        current_window = discount[i:i + window_size]
        current_count = Counter(current_window)
        
        if all(current_count.get(item, 0) >= want_dict[item] for item in want_dict):
            result += 1
    
    return result