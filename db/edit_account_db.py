import random
import string
import MySQLdb

from function import user_function

from db import connect_db


# アカウントの取得
def search_account(user_id, pw=None):
    conn = connect_db.get_select_connection()
    cur = conn.cursor(MySQLdb.cursors.DictCursor)

    if pw:
        salt = search_salt(user_id)

        if salt is None:
            return False

        # ハッシュ化の関数
        hashed_pw = user_function.hash(salt, pw)

        sql = 'select user_id, mail, user_name from users where user_id = %s AND password = %s'

        try:
            cur.execute(sql, (user_id, hashed_pw))
        except Exception as e:
            return False
    else:
        sql = 'select user_id, mail, user_name from users where user_id = %s'

        try:
            cur.execute(sql, (user_id,))
        except Exception as e:
            return False

    account = cur.fetchone()

    cur.close()
    conn.close()

    return account


# ソルトの取得
def search_salt(user_id):
    conn = connect_db.get_select_connection()
    cur = conn.cursor()

    sql = 'select salt from users where user_id = %s'

    try:
        cur.execute(sql, (user_id,))
    except Exception as e:
        return False

    salt = cur.fetchone()

    cur.close()
    conn.close()

    return salt[0]


# アカウントの編集
def update_account(user_id, user_name, pw):
    salt = "".join(random.choices(string.ascii_letters, k=32))
    hashed_pw = user_function.hash(salt, pw)

    conn = connect_db.get_update_connection()
    cur = conn.cursor()

    sql = "UPDATE users SET user_name = %s, password = %s, salt = %s WHERE user_id = %s"

    try:
        cur.execute(sql, (user_name, hashed_pw, salt, user_id))
    except Exception as e:
        return False

    cur.close()
    conn.commit()
    conn.close()

    return True
