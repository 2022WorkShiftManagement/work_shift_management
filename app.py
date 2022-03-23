from flask import Flask, render_template, session
from view.create_account import create_account
from view.login import login
from view.group import group
from view.add_job import add_job
from view.edit_account import edit_account
from view.edit_job import edit_job


app = Flask(__name__)

# グループ作成

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
