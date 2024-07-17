def solution(board, k):
    answer = 0
    for x in range(len(board)):
        for y in range(len(board[0])):
            if x + y <= k:
                answer += board[x][y]
                
    return answer