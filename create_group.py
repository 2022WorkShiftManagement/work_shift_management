from flask import Flask, Blueprint, render_template, redirect, request, url_for, session

create_group = Blueprint('create_group', __name__, url_prefix='/create-group')


@create_group.route("/", methods=['GET', 'POST'])
def create_group_form():
    # if "user_id" not in session:  # セッションの有無
    # return redirect("/")
    if request.method == 'GET':
        return render_template("create_group.html")
    elif request.method == 'POST':
        group_name = request.form.get('group_name')
        if group_name is None or group_name == '':  # グループ名が入力されていなかった場合
            message = 'グループ名が入力されていません'
            return render_template('create_group.html', alert_message=message)
        else:
            message = "グループ名: " + group_name
            return render_template('create_group.html', alert_message=message)
