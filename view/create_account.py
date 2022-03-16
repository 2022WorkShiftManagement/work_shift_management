from flask import Blueprint, render_template, request, session, redirect, url_for
from db import create_account_db

create_account = Blueprint('create_account', __name__)


# アカウント作成ページ
@create_account.route("/create_account")
def create_account_page():
    error = request.args.get('error')
    return render_template('create_account.html', account=session.get("account"), error=error)


# アカウント確認ページ
@create_account.route("/confirm_account", methods=["POST"])
def confirm_account_page():
    mail = request.form.get("mail")
    name = request.form.get("name")
    pw = request.form.get("pw")

    if mail and name and pw:
        session['account'] = {
            'mail': mail,
            'name': name,
            'pw': pw,
        }
        return render_template('confirm_account.html', mail=mail, name=name)

    return redirect("/create_account")


@create_account.route("/insert_account")
def insert_account_page():
    if not create_account_db.insert_account(session['account']):
        redirect(url_for('create_account_page', error='アカウント登録に失敗しました'))

    session.pop('account', None)

    return redirect("/")
