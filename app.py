from flask import Flask, render_template, session, request
import os
from datetime import timedelta

from view.create_account import create_account
from view.login import login
from view.group import group
from view.job import job
from view.edit_account import edit_account


app = Flask(__name__)

# セッション有効化のために鍵を設定
app.secret_key = os.environ['SECRET_KEY']
# セッションの有効時間を設定、15分間何も操作がなければ自動ログアウト
app.permanent_session_lifetime = timedelta(minutes=15)


@app.route("/")
def index():
    error = request.args.get('error')
    session.pop('account', None)
    return render_template('index.html', error=error)


# アカウント作成ページ
app.register_blueprint(create_account)
# ログインページ
app.register_blueprint(login)
# バイト先ページ
app.register_blueprint(job)
# グループページ
app.register_blueprint(group)
# アカウント編集ページ
app.register_blueprint(edit_account)

if __name__ == "__main__":
    app.run(debug=True)
