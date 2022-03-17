from flask import Blueprint, render_template, request, session, redirect, url_for

from db.group_db import create_group, select_group

group = Blueprint('group', __name__, url_prefix='/group')


@group.route("/newGroup", methods=['GET', 'POST'])
def create_group_form():
    if "user_id" not in session:  # セッションの有無
        return redirect("/")
    if request.method == 'POST':
        group_name = request.form.get('group_name')
        if group_name:
            random_string = create_group(group_name)
            if random_string:
                return redirect(url_for('group.group_detail', gid=random_string))
            else:
                message = 'グループ作成出来ませんでした'
        else:
            message = 'グループ名が入力されていません'
        return render_template('create_group.html', alert_message=message)
    else:
        return render_template("create_group.html")


@group.route('/detail/<string:gid>', methods=["POST", "GET"])
def group_detail(gid):
    if "user_id" not in session:  # セッションの有無
        return redirect("/")
    print('group_ID:' + gid)
    group_details = select_group(gid)
    if group_details:
        return render_template('group_detail.html', details=group_details)
    else:
        return render_template('group_detail.html', alert_message="グループが無いよ")
