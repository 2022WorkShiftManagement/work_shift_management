import MySQLdb
from db import connect_db


# バイト先情報を登録
def insert_work_shift_info(user_id, job_name, color):
    conn = connect_db.get_update_connection()
    cur = conn.cursor()

    sql = "INSERT INTO job_infos(user_id, job_name, color_code) VALUES(%s, %s, %s)"

    try:
        cur.execute(sql, (user_id, job_name, int(color, 16)))
    except Exception as e:
        return False

    cur.close()
    conn.commit()
    conn.close()

    return True


# ユーザの登録しているバイト先を取得
def get_user_job(user_id):
    conn = connect_db.get_update_connection()
    cur = conn.cursor(MySQLdb.cursors.DictCursor)

    sql = "SELECT job_id, job_name, LPAD(HEX(color_code), 6, '0') AS color FROM job_infos WHERE user_id = %s AND delete_flg = 0"

    try:
        cur.execute(sql, (user_id,))
    except Exception as e:
        return False

    job_list = list(cur.fetchall())

    cur.close()
    conn.close()

    return job_list


# バイト先情報を編集
def update_job(user_id, job_id, job_name, color):
    conn = connect_db.get_update_connection()
    cur = conn.cursor()

    sql = "UPDATE job_infos SET job_name = %s, color_code = %s WHERE user_id = %s and job_id = %s"

    try:
        cur.execute(sql, (job_name, int(color, 16), user_id, job_id))
    except Exception as e:
        print(e)
        return False

    cur.close()
    conn.commit()
    conn.close()

    return True
