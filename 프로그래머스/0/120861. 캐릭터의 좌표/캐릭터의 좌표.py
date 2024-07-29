def solution(keyinput, board):
    x_max = board[0] // 2
    y_max = board[1] // 2

    result = [0, 0]
    for i in keyinput:
        if i == 'left' and result[0] > x_max * -1:
            result[0] -= 1
        elif i == 'right' and result[0] < x_max:
            result [0] += 1
        elif i == 'down' and result[1] > y_max * -1:
            result[1] -= 1
        elif i == 'up' and result[1] < y_max:
            result[1] += 1
        else:
            continue
    return result