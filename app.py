from datetime import timedelta

import os
from flask import Flask, Blueprint, render_template

from view.add_work_shift_info_page import add_work_shift_info


app = Flask(__name__)

# セッション有効化のために鍵を設定
app.secret_key = 'hogehoge'


@app.route("/")
def index():
    return render_template('index.html')


app.register_blueprint(add_work_shift_info)


if __name__ == "__main__":
    app.run(debug=True)
