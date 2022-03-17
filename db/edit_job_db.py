from work_shift_management.db import connect_db


def get_user_job(user_id):
    conn = connect_db.get_update_connection()
    cur = conn.cursor()

    sql = "SELECT job_id, job_name, color_code FROM job_infos WHERE user_id = %s AND delete_flg = 0"

    try:
        cur.execute(sql, (user_id,))
    except Exception as e:
        return False

    job_list = cur.fetchall()

    cur.close()
    conn.close()

    return job_list
