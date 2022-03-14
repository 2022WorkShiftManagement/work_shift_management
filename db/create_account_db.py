import MySQLdb
import hashlib
import random
import string


# ユーザ情報取得処理
def insert_account(account):
    salt = "".join(random.choices(string.ascii_letters, k=32))
    b_pw = bytes(account['pw'], 'utf-8')
    b_salt = bytes(salt, 'utf-8')
    hashed_pw = hashlib.pbkdf2_hmac("sha256", b_pw, b_salt, 2560).hex()

    conn = get_connection()
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
def get_connection():
    return MySQLdb.connect(user='root', passwd='lamia6405',host='localhost', db='work_shift_management',
                           charset="utf8")
