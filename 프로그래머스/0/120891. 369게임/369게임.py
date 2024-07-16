def solution(order):
    clap = ['3', '6', '9']
    result = 0
    for i in clap:
        result += str(order).count(i)
    return result