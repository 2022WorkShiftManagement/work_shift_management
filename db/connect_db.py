import os
import MySQLdb


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
