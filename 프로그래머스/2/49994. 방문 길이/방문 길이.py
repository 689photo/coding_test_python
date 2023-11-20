def solution(dirs):
    loca = [0, 0]
    history = []
    answer = 0
    
    for i in dirs:
        if i == 'L':
            if loca[1] > -5 and loca[1] <= 5:
                movement = [loca[0], loca[0], min(loca[1], loca[1] - 1), max(loca[1], loca[1] - 1)]
                if movement not in history:
                    answer += 1
                    history.append(movement)
                loca[1] -= 1
        elif i == 'R':
            if loca[1] >= -5 and loca[1] < 5:
                movement = [loca[0], loca[0], min(loca[1], loca[1] + 1), max(loca[1], loca[1] + 1)]
                if movement not in history:
                    answer += 1
                    history.append(movement)
                loca[1] += 1
        elif i == 'U':
            if loca[0] >= -5 and loca[0] < 5:
                movement = [min(loca[0], loca[0] + 1), max(loca[0], loca[0] + 1), loca[1], loca[1]]
                if movement not in history:
                    answer += 1
                    history.append(movement)
                loca[0] += 1
        elif i == 'D':
            if loca[0] > -5 and loca[0] <= 5:
                movement = [min(loca[0], loca[0] - 1), max(loca[0], loca[0] -1 ), loca[1], loca[1]]
                if movement not in history:
                    answer += 1
                    history.append(movement)
                loca[0] -= 1

    return answer