def solution(msg):
    answer = []
    
    alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    dic = {}
    
    for x, y in zip(alp, num):
        dic[x] = y

    while msg:
        for i in range(len(msg),0,-1):
            if msg[:i] in dic:
                answer.append(dic[msg[:i]])
                dic[msg[:i+1]] = len(dic) + 1
                msg = msg[i:]
                break
    return answer