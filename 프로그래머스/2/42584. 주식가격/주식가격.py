def solution(prices):
    answer = []
    for x in range(len(prices) -1):
        sec = 0
        for y in range(x, len(prices) -1):
            if prices[x] > prices[y]:
                break
            sec += 1
        answer.append(sec)
    answer.append(0)
    
    return answer
            