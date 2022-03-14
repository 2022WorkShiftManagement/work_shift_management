import random
import string
from flask import Blueprint, render_template, request, session, redirect

from connect_db import connect_db

group = Blueprint('group', __name__, url_prefix='/group')


@group.route("/newGroup", methods=['GET', 'POST'])
def create_group_form():
    # if "user_id" not in session:  # セッションの有無
    # return redirect("/")

    if request.method == 'POST':
        group_name = request.form.get('group_name')
        if group_name is None or group_name == '':  # グループ名が入力されていなかった場合
            message = 'グループ名が入力されていません'
            return render_template('create_group.html', alert_message=message)
        else:
            random_string = randomstring(16)
            conn = connect_db()
            cur = conn.cursor()
            # グループの作成
            sql = "INSERT INTO usergroups(user_id, group_name, group_string) VALUES(%s,%s,%s)"
            # グループへの参加
            sql2 = '''INSERT INTO joininggroups(user_id, group_id)
                        VALUES (%s,
                            (SELECT group_id FROM usergroups
                            WHERE group_string = %s
                        ));'''
            try:
                cur.execute(sql, (1, group_name, random_string))
                cur.execute(sql2, (1, random_string))
                conn.commit()
            except Exception as e:
                message = "作成出来ませんでした。"
                return render_template('create_group.html', alert_message=message)
            cur.close()
            conn.close()
            return render_template('', )

    else:
        return render_template("create_group.html")


def randomstring(n):
    random_string = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    return ''.join(random_string)
