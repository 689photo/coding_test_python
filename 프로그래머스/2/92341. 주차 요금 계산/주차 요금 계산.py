from math import ceil
def solution(fees, records):
    time = {}
    fee = {}
    
    for i in records:
        temp = 0
        car = i[6:10]
        if 'IN' in i:
            time[car] = int(i[:2]) * 60 + int(i[3:5])
        else:
            temp = int(i[:2]) * 60 + int(i[3:5]) - time[car]
            del time[car]
            if car in fee:
                fee[car] += temp
            else:
                fee[car] = temp
    
    if time:
        for i in time.items():
            car = i[0]
            if car in fee:
                fee[car] += 1439 - i[1]
            else:
                fee[car] = 1439 - i[1]
                
    for i in fee.items():
        car = i[0]
        if i[1] <= fees[0]:
            fee[car] = fees[1]
        else:
            fee[car] = (ceil((i[1] -fees[0]) / fees[2]) * fees[3]) + fees[1]
    
    
    return list(i[1] for i in sorted(fee.items(), key=lambda x: x[0]))