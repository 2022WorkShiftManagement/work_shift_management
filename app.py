from flask import Flask, render_template, session
from view.create_account import create_account
from view.login import login
from view.group import group
import os

app = Flask(__name__)

# グループ作成

# セッション有効化のために鍵を設定
app.secret_key = 'hogehoge'


# グループ作成
app.register_blueprint(group)

@app.route("/")
def index():
    session.pop('account', None)
    return render_template('index.html')


# アカウント作成ページ
app.register_blueprint(create_account)
# ログインページ
app.register_blueprint(login)


if __name__ == "__main__":
    app.run(debug=True)
