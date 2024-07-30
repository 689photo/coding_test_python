def solution(id_pw, db):
    db = dict(db)
    
    if id_pw[0] not in db:
        return 'fail'
    elif db[id_pw[0]] != id_pw[1]:
        return 'wrong pw'
    else:
        return 'login'