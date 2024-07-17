def solution(numbers):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    answer = 0
    
    for i in num:
        if i not in numbers:
            answer += i
    return answer