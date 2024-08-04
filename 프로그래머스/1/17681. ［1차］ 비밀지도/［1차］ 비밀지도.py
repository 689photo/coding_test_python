def solution(n, arr1, arr2):
    
    for i in range(len(arr1)):
        arr1[i] = str(bin(arr1[i])[2:]).zfill(n)
        
    for i in range(len(arr2)):
        arr2[i] = str(bin(arr2[i])[2:]).zfill(n)
    
    arr3 = []
    
    for x, y in zip(arr1, arr2):
        temp = ''
        for a, e in zip(x, y):
            if a == '0' and e == '0':
                temp += ' '
            else:
                temp += '#'
        arr3.append(temp)
    
    return arr3