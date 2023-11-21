from itertools import permutations
def solution(numbers):
    lst = set()
    answer = 0
    for i in range(1, len(numbers)+1):
        temp = list(permutations(list(numbers), i))
        for x in temp:
            num = int(''.join(x))
            if num >= 2:
                lst.add(num)
    
    for i in list(lst):
        for x in range(2, int(i**0.5)+1):
            if i % x == 0:
                break
        else:
            answer += 1
    
    return answer
            