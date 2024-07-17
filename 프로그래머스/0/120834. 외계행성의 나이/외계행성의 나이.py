def solution(age):
    alp = 'abcdefghij'
    result = ""
    
    for i in str(age):
        result += alp[int(i)]
    return result