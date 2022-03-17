from datetime import timedelta

import os
from flask import Flask, Blueprint, render_template

from view.add_job import add_job

from view.edit_job import edit_job

app = Flask(__name__)

# セッション有効化のために鍵を設定
app.secret_key = 'hogehoge'


@app.route("/")
def index():
    return render_template('index.html')


# バイト先情報登録画面
app.register_blueprint(add_job)
# バイト先情報編集画面
app.register_blueprint(edit_job)


if __name__ == "__main__":
    app.run(debug=True)
