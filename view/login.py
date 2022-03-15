from flask import Blueprint, render_template, request, session, redirect, url_for
from db import login_db

login = Blueprint('login', __name__)


# ログインページ
@login.route("/top", methods=["POST"])
def top_page():
    mail = request.form.get('mail')
    pw = request.form.get('pw')

    user_id = login_db.login(mail, pw)
    print(user_id)
    if user_id is None:
        return redirect("/")

    session['user'] = user_id

    return render_template('test.html')
