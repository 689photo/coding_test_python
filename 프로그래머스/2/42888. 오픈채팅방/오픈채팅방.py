def solution(record):
    user = {}
    result = []
    answer = []
    for i in record:
        i = i.split()
        if 'Enter' in i:
            uid = i[1]
            user[uid] = i[2]
            result.append(uid + ",님이 들어왔습니다.")
            
        elif 'Leave' in i:
            uid = i[1]
            result.append(uid + ",님이 나갔습니다.")
            
        else:
            uid = i[1]
            user[uid] = i[2]
    
    for i in result:
        i = i.split(',')
        answer.append(user[i[0]]+i[1])
    
    return answer