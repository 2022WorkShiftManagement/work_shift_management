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
