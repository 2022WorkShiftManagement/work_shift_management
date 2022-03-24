import MySQLdb
import hashlib
import random
import string
import os
from function import user_function as uf
from db import connect_db


# ユーザ情報取得処理
def insert_account(account):
    salt = "".join(random.choices(string.ascii_letters, k=32))

    # ハッシュ化の関数
    hashed_pw = uf.hash(salt, account['pw'])

    conn = connect_db.get_update_connection()
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
