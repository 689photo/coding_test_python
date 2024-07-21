def solution(myStr):
    te = ['a', 'b', 'c']
    for i in te:
        myStr = myStr.replace(i, ' ')
    myStr = myStr.split()
    
    if myStr == []:
        return ['EMPTY']
    return myStr