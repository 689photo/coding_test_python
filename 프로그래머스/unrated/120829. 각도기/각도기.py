def solution(angle):
    if angle == 180:
        return 4
    elif 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    else:
        return 3