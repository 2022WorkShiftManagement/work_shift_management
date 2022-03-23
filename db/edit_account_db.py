import random
import string

from function import user_function

import connect_db


# アカウントの取得
def search_account(user_id):
    conn = connect_db.get_select_connection()
    cur = conn.cursor()

    sql = 'select user_id, mail, user_name from users where user_id = %s'

    try:
        cur.execute(sql, (user_id,))
    except Exception as e:
        return False

    account = cur.fetchone()

    cur.close()
    conn.close()

    return account


# アカウントの編集
def update_account(user_id, user_name, pw):
    salt = "".join(random.choices(string.ascii_letters, k=32))
    hashed_pw = user_function.hash(salt, pw)

    conn = connect_db.get_update_connection()
    cur = conn.cursor()

    sql = "UPDATE job_infos SET user_name = %s, password = %s WHERE user_id = %s"

    try:
        cur.execute(sql, (user_name, hashed_pw, user_id))
    except Exception as e:
        return False

    cur.close()
    conn.commit()
    conn.close()

    return True
