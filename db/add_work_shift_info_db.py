import MySQLdb
import os


# バイト先情報を登録
def insert_work_shift_info(user_id, job_name, color):
    conn = get_update_connection()
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


# DBとのコネクションを取得
def get_select_connection():
    # 環境変数の取得
    pw = os.environ['DATABASE_PASS']

    return MySQLdb.connect(
        user='select_user',
        passwd=pw,
        host='localhost',
        db='work_shift_management',
        charset="utf8"
    )


def get_update_connection():
    # 環境変数の取得
    pw = os.environ['DATABASE_PASS']

    return MySQLdb.connect(
        user='update_user',
        passwd=pw,
        host='localhost',
        db='work_shift_management',
        charset="utf8"
    )
