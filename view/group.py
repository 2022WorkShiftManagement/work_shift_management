from flask import Blueprint, render_template, request, session, redirect, url_for

from db.group_db import (
    create_group,
    select_group,
    select_member_count,
    entry_group_confirmation,
    join_group,
    remove_member,
    delete_group_db,
    update_group
)

group = Blueprint('group', __name__, url_prefix='/group')


@group.route("/newGroup", methods=['GET', 'POST'])
def create_group_form():
    if "user" not in session:  # セッションの有無
        return redirect("/")
    if request.method == 'POST':
        group_name = request.form.get('group_name')
        if group_name:
            random_string = create_group(session['user'], group_name)
            if random_string:
                return redirect(url_for('group.group_detail', gid=random_string))
            else:
                message = 'グループ作成出来ませんでした'
        else:
            message = 'グループ名が入力されていません'
        return render_template('create_group.html', alert_message=message)
    else:
        return render_template("create_group.html")


@group.route('/detail/<string:gid>', methods=['GET', 'POST'])
def group_detail(gid):
    if "user" not in session:  # セッションの有無
        return redirect("/")
    group_details = select_group(gid)
    member_count = select_member_count(gid)
    if request.method == 'POST':
        group_name = request.form.get('new_group_name')
        update_group(gid, group_name)
    if group_details:
        joining_already = entry_group_confirmation(session['user'], gid)
        if joining_already:
            return render_template('group_detail.html', details=group_details)
        else:
            return render_template('group_entry.html', details=group_details, member_count=member_count)
    else:
        return render_template('group_detail.html', alert_message="グループが存在しません")


@group.route('/entry/<string:gid>')
def group_entry(gid):
    if "user" not in session:
        return redirect("/")
    entry_ok = join_group(session['user'], gid)
    if entry_ok:
        return redirect(url_for('group.group_detail', gid=gid))
    return render_template('group_entry.html', alert_message='entry_error')


@group.route('/remove_member/<string:gid>/<int:uid>')
def remove_group(uid, gid):
    if "user" not in session:
        return redirect("/")
    remove_member(uid, gid)
    return redirect(url_for('group.group_detail', gid=gid))


@group.route('/delete_group/<string:gid>')
def delete_group(gid):
    if "user" not in session:
        return redirect("/")
    delete_ok = delete_group_db(gid)
    if delete_ok:
        return redirect("/home")
    return redirect(url_for('group.group_detail', gid=gid))
