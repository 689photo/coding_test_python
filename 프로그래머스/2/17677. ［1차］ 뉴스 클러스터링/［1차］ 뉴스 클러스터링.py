import re
def solution(str1, str2):
    p = re.compile('^[a-z]+$')
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1 = list(str1[i] + str1[i+1] for i in range(0, len(str1) - 1))
    str2 = list(str2[i] + str2[i+1] for i in range(0, len(str2) - 1))
    
    str1 = list(filter(p.match, str1))
    cp1 = str1[:]
    str2 = list(filter(p.match, str2))
    cp2 = str2[:]
    
    if str1 == [] and str2 == []:
        return 65536
    
    inter = []
    for i in cp1:
        if i in cp2:
            inter.append(i)
            
            cp2.remove(i)
    print(inter)
            
    summ = len(str1) + len(str2) - len(inter)
    
    return int((len(inter) / summ) * 65536)