import re
def solution(files):
    lst = [re.split('([0-9]+)', file) for file in files]
    lst.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(i) for i in lst]