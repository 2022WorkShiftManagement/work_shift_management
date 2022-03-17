import MySQLdb
import hashlib
import random
import string
import os
from function import user_function


# ユーザ情報取得処理
def insert_account(account):
    salt = "".join(random.choices(string.ascii_letters, k=32))

    # ハッシュ化の関数
    hashed_pw = user_function.hash(salt, account['pw'])

    conn = get_update_connection()
    cur = conn.cursor()

    sql = "INSERT INTO users(mail, password, salt, user_name) VALUES(%s, %s, %s, %s)"

    try:
        cur.execute(sql, (account['mail'], hashed_pw, salt, account['name']))
    except Exception as e:
        print("SQL実行に失敗：", e)
        return False

    cur.close()
    conn.commit()
    conn.close()

    return True


# DBとのコネクションを取得
def get_select_connection():
    # 環境変数の取得
    pw = os.environ['DATABASE_PASS']

    return MySQLdb.connect(user='select_user', passwd=pw, host='localhost', db='work_shift_management',
                           charset="utf8")


def get_update_connection():
    # 環境変数の取得
    pw = os.environ['DATABASE_PASS']

    return MySQLdb.connect(user='update_user', passwd=pw, host='localhost', db='work_shift_management',
                           charset="utf8")