import random
import string
from flask import Blueprint, render_template, request, session, redirect, url_for

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
            return redirect(url_for('group.group_detail', gid=random_string))

    else:
        return render_template("create_group.html")



@group.route('/detail/<string:gid>', methods=["POST", "GET"])
def group_detail(gid):
    # if "user_id" not in session:  # セッションの有無
    # return redirect("/")
    print('group_ID:' + gid)

    sql = '''SELECT jg.user_id, user_name, jg.group_id, ug.user_id as group_reader, group_name, group_string FROM joininggroups as jg
        INNER JOIN users as us ON us.user_id = jg.user_id
        INNER JOIN usergroups as ug ON ug.group_id = jg.group_id
        WHERE us.delete_flg=0 AND ug.group_string=%s'''

    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(sql, (gid,))
        group_details = cur.fetchall()
        print(group_details)
        cur.close()
        conn.close()
        return render_template('group_detail.html', details=group_details)
    except Exception as e:
        return render_template('group_detail.html', alert_message="グループが無いよ")

def randomstring(n):
    random_string = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    return ''.join(random_string)
