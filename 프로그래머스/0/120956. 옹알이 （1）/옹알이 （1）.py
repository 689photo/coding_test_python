def solution(babbling):
    result = 0
    say = ['aya', 'ye', 'woo', 'ma']
    
    for i in babbling:
        for s in say:
            if i == s:
                result += 1
                break
            else:
                i = i.replace(s, ' ')
        if not i.strip():
            result += 1
    return result