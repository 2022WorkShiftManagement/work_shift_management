from flask import Blueprint, render_template, request, session, redirect, url_for
from db import edit_job_db

edit_job = Blueprint('edit_job', __name__)


# バイト先情報登録画面
@edit_job.route("/edit_job")
def edit_job_page():
    if "user" not in session:
        return redirect("/")
    else:
        error = request.args.get('error')

        job_list = edit_job_db.get_user_job(session['user_id'])
        for job in job_list:
            job['color_name'] = get_color(job['color'])

        print(job_list)
        return render_template(
            'edit_job.html',
            job_list=job_list,
            color_list=get_color(),
            error=error
        )


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
