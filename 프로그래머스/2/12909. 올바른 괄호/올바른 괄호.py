def solution(s):
    answer = []
    for i in s:
        if i == "(":
            answer.append("(")
        else:
            if answer == []:
                return False
            else:
                answer.pop()
    return answer == []
        