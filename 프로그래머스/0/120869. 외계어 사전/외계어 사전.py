def solution(spell, dic):
    spell.sort()
    for i in dic:
        if sorted(list(i)) == spell:
            return 1
    return 2