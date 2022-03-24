from flask import Flask, render_template, session, request
from view.create_account import create_account
from view.login import login
from view.group import group
from view.job import job
from view.edit_account import edit_account
from view.home import home


app = Flask(__name__)

# グループ作成

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
# バイト先ページ
app.register_blueprint(job)
# グループページ
app.register_blueprint(group)
# アカウント編集ページ
app.register_blueprint(edit_account)

app.register_blueprint(home)


if __name__ == "__main__":
    app.run(debug=True)
