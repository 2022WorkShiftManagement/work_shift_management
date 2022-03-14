from flask import Flask, render_template
from view.create_account import create_account

app = Flask(__name__)

# セッション有効化のために鍵を設定
app.secret_key = 'hogehoge'


@app.route("/")
def index():
    return render_template('index.html')


# アカウント作成ページ
app.register_blueprint(create_account)

if __name__ == "__main__":
    app.run(debug=True)
