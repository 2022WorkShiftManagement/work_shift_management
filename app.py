from datetime import timedelta

import os
from flask import Flask, Blueprint, render_template
from view.home import home

app = Flask(__name__)

app.register_blueprint(home)

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
