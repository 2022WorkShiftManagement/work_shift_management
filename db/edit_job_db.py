import MySQLdb

from db import connect_db


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
