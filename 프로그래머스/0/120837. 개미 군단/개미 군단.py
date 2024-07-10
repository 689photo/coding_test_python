def solution(hp):
    ant = [5, 3, 1]
    answer = 0
    
    for i in ant:
        answer += hp // i
        if hp % i == 0:
            break
        else:
            hp = hp % i
    
    return answer