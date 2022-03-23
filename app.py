from flask import Flask, render_template, session
import os
from datetime import timedelta

from view.create_account import create_account
from view.login import login
from view.group import group
from view.add_job import add_job
from view.edit_account import edit_account
from view.edit_job import edit_job


app = Flask(__name__)

# セッション有効化のために鍵を設定
app.secret_key = os.environ['SECRET_KEY']
# セッションの有効時間を設定、15分間何も操作がなければ自動ログアウト
app.permanent_session_lifetime = timedelta(minutes=15)


@app.route("/")
def index():
    session.pop('account', None)
    return render_template('index.html')


# アカウント作成ページ
app.register_blueprint(create_account)
# ログインページ
app.register_blueprint(login)
# バイト先情報登録画面
app.register_blueprint(add_job)
# グループページ
app.register_blueprint(group)
# アカウント編集ページ
app.register_blueprint(edit_account)
# バイト先情報編集画面
app.register_blueprint(edit_job)


if __name__ == "__main__":
    app.run(debug=True)
