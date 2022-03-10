import MySQLdb


def connect_db():
    conn = MySQLdb.connect(
        host='127.0.0.1',  # localhostでもOK
        user='root',
        passwd='password',
        db='work_shift_management',
        charset='utf8'
    )
    return conn
