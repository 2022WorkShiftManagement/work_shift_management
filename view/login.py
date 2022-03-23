from flask import Blueprint, render_template, request, session, redirect, url_for
from db import login_db
from function import user_function as uf

login = Blueprint('login', __name__)


# ログインページ
@login.route("/home_post", methods=["POST"])
def home_post_page():
    mail = request.form.get('mail')
    pw = request.form.get('pw')

    if not uf.mail_validation(mail):
        return redirect(url_for('index', error='メールを正しく入力してください'))

    elif not uf.pw_validation(pw):
        return redirect(url_for('index', error='パスワードを正しく入力してください'))

    else:
        user_id = login_db.login(mail, pw)

    if user_id is None:
        return redirect("/")

    session['user'] = user_id

    return render_template('home.html')


# sessionが残っていれば直でhome.htmlに遷移
@login.route("/home_get", methods=["GET"])
def home_get_page():
    if 'user' in session:
        return render_template('home.html')

    return redirect('/home_post')
