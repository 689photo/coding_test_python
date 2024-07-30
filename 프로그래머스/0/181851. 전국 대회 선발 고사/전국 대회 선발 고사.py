def solution(rank, attendance):
    lst = sorted([rank[i] for i in range(len(rank)) if attendance[i] == True])
    
    return 10000 * rank.index(lst[0]) + 100 * rank.index(lst[1]) + rank.index(lst[2])