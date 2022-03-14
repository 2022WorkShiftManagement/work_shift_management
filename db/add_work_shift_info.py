import MySQLdb

def insert_work_shift_info(user_id, job_name, color):
    conn = get_connection()
    cur = conn.cursor()

    sql = "INSERT INTO jobInfos(user_id, job_name, color_code) VALUES(%s, %s, %s)"

    try:
        cur.execute(sql, (user_id, job_name, color))
    except Exception as e:
        return False

    cur.close()
    cur.commit()
    conn.close()

    return True

def get_connection():
    return MySQLdb.connect(
        user='root',
        passwd="@Amuamu923",
        host='160.251.41.18',
        db='work_shift_management',
        charset="utf8"
    )
