from flask import Flask, render_template, session
from view.create_account import create_account
from view.login import login
from view.add_job import add_job


app = Flask(__name__)

# セッション有効化のために鍵を設定
app.secret_key = 'hogehoge'


@app.route("/")
def index():
    session.pop('account', None)
    return render_template('index.html')



# アカウント作成ページ
app.register_blueprint(create_account)
# ログインページ
app.register_blueprint(login)
# バイト先情報登録ページ
app.register_blueprint(add_job)


if __name__ == "__main__":
    app.run(debug=True)
