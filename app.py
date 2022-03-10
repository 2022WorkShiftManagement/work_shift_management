from datetime import timedelta

import os
from flask import Flask, Blueprint, render_template

from create_group import create_group

app = Flask(__name__)

# グループ作成
app.register_blueprint(create_group)

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
