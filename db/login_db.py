import MySQLdb
import hashlib
import os
from function import user_function


def login(mail, pw):
    salt = search_salt(mail)

    if salt is None:
        return None

    # ハッシュ化の関数
    hashed_pw = user_function.hash(salt, pw)

    user_id = search_account(mail, hashed_pw)

    return user_id


def search_salt(mail):
    conn = get_select_connection()
    cur = conn.cursor()

    sql = 'select salt from users where mail = %s'

    try:
        cur.execute(sql, (mail,))
    except Exception as e:
        print('sql実行に失敗', e)
        return False

    salt = cur.fetchone()

    cur.close()
    conn.close()

    if salt:
        return salt[0]

    return None


def search_account(mail, pw):
    conn = get_select_connection()
    cur = conn.cursor()

    sql = 'select user_id from users where mail = %s and password = %s'

    try:
        cur.execute(sql, (mail, pw,))
    except Exception as e:
        print('sql実行に失敗', e)
        return None

    user_id = cur.fetchone()

    cur.close()
    conn.close()

    return user_id


# DBとのコネクションを取得
def get_select_connection():
    # 環境変数の取得
    host = os.environ['DATABASE_HOST']
    pw = os.environ['DATABASE_PASS']

    return MySQLdb.connect(user='select_user', passwd=pw, host=host, db='work_shift_management',
                           charset="utf8")


def get_update_connection():
    # 環境変数の取得
    host = os.environ['DATABASE_HOST']
    pw = os.environ['DATABASE_PASS']

    return MySQLdb.connect(user='update_user', passwd=pw, host=host, db='work_shift_management',
                           charset="utf8")
