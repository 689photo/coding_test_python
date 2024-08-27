def solution(N, stages):
    stage = dict(zip(range(1, N+1), [0] * N))
    
    for i in range(1, N+1):
        user = 0
        fail = 0
        for a in stages:
            if a >= i:
                user += 1
                if a == i:
                    fail += 1
        stage[i] = fail / user if user != 0 else 0
    
    stage = sorted(stage.items(), key=lambda x:x[1], reverse=True)
    return [i[0] for i in stage]