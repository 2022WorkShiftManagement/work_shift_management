from flask import Flask, render_template, session, request
from view.create_account import create_account
from view.login import login
import os

app = Flask(__name__)

# セッション有効化のために鍵を設定
app.secret_key = 'hogehoge'


@app.route("/")
def index():
    error = request.args.get('error')
    session.pop('account', None)
    return render_template('index.html', error=error)


# アカウント作成ページ
app.register_blueprint(create_account)
# ログインページ
app.register_blueprint(login)


if __name__ == "__main__":
    app.run(debug=True)
