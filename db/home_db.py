import os
import MySQLdb

def get_join_groups(id: str):
    """
    現在の最新のユーザーIDを取得
    Args:
    id: str
    Returns:
      自分が所属しているグループとその一覧
    """

    conn = get_select_connection()
    cur = conn.cursor()

    cur.execute('''SELECT a.user_id,u.user_name, b.group_id, c.group_name FROM joining_groups AS a 
    INNER JOIN (SELECT group_id FROM joining_groups WHERE user_id = (%s)) AS b ON b.group_id = a.group_id LEFT
    OUTER JOIN user_groups as c on c.group_id = b.group_id LEFT OUTER JOIN users as u on u.user_id = a.user_id;  ORDER BY group_id''',(1,))

    group_list = cur.fetchall()

    return group_list


# DBとのコネクションを取得
def get_select_connection():
    # 環境変数の取得
    host = 'db'
    pw = os.environ['DATABASE_PASS']

    return MySQLdb.connect(user='select_user', passwd=pw, host=host, db='work_shift_management',
                           charset="utf8")



