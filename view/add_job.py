from flask import Blueprint, render_template, request, session, redirect, url_for
from db import add_job_db

add_job = Blueprint('add_job', __name__)


# バイト先情報登録画面
@add_job.route("/add_job")
def add_job_page():
    session['user'] = 1
    if "user" not in session:
        return redirect("/")
    else:
        session['job'] = {
            'name': None,
            'color_code': None,
            'color_name': None
        }
        error = request.args.get('error')
        return render_template(
            'add_job.html',
            color=get_color(),
            error=error
        )


# バイト先情報登録確認画面
@add_job.route("/confirm_job", methods=["POST"])
def confirm_job_page():
    if "user" not in session:
        return redirect("/")
    else:
        job_name = request.form.get('job_name')
        job_color = request.form.get('color')

        # 入力チェック
        if job_name and job_color:
            session['job'] = {
                'name': job_name,
                'color_code': job_color,
                'color_name': get_color(job_color)
            }

            return render_template('confirm_add_job.html')

        # 入力に不備があったら入力画面へリダイレクト
        return redirect(
            url_for(
                'add_job.add_job_page',
                error='入力内容に不備があります。'
            )
        )


# バイト先情報登録
@add_job.route("/insert_job")
def insert_job():
    if "user" not in session:
        return redirect("/")
    else:
        insert_result = add_job_db.insert_work_shift_info(
            session['user'],
            session['job']['name'],
            session['job']['color_code']
        )

        # データベースに登録できたか
        if insert_result:
            return redirect("/home")

        return redirect(
            url_for(
                'add_job.add_job_page',
                error='登録に失敗しました。'
            )
        )


# シフト表示画面（仮）
@add_job.route("/home")
def home():
    return "test"


# 選択するカラーを取得
def get_color(key=None):
    color = {
        "FF0000": "レッド",
        "FF3399": "ピンク",
        "FF9100": "オレンジ",
        "FFD400": "イエロー",
        "008000": "グリーン",
        "B2D235": "イエローグリーン",
        "67A7CC": "スカイブルー",
        "0067C0": "ブルー",
        "5F4894": "パープル",
        "717375": "グレー"
    }

    if key:
        return color[key]

    return color
