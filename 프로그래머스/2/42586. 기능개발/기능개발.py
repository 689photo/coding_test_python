def solution(progresses, speeds):
    result = []
    while len(progresses) > 0:
        before = len(progresses)
        for x, y in enumerate(progresses):
            progresses[x] = y + speeds[x]
        if progresses[0] >= 100:
            while len(progresses) > 0 and progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
            result.append(before - len(progresses))
    return result