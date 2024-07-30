def solution(score):
    member = [sum(i) / 2 for i in score]
    rank = sorted(member, reverse=True)
      
    return [rank.index(i) + 1 for i in member]