def solution(a, b):
    answer = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    
    return answer[(sum(month[:a]) + b) % 7]