from datetime import timedelta

import os
from flask import Flask, Blueprint, render_template

from group import group

app = Flask(__name__)

# グループ作成
app.register_blueprint(group)

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
