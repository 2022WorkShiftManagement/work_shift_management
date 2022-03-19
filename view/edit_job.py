from flask import Blueprint, render_template, request, session, redirect, url_for
from db import edit_job_db
from function.color import get_color

edit_job = Blueprint('edit_job', __name__)


# バイト先情報編集画面
@edit_job.route("/edit_job")
def edit_job_page():
    if "user" not in session:
        return redirect("/")
    else:
        error = request.args.get('error')

        # ユーザの登録しているバイト先を取得
        job_list = edit_job_db.get_user_job(session['user'])

        # 取得できなかった時
        if not job_list:
            redirect("/home")

        # バイトの色を取得
        for job in job_list:
            job['color_name'] = get_color(job['color'])

        return render_template(
            'edit_job.html',
            job_list=job_list,
            color_list=get_color(),
            error=error
        )


# バイト先情報編集確認画面
@edit_job.route("/confirm_edit_job", methods=["POST"])
def confirm_edit_job_page():
    if "user" not in session:
        return redirect("/")
    else:
        job_id = request.form.get("edit_job")
        job_name = request.form.get("job_name")
        color = request.form.get("color")

        # 入力チェック
        if job_id and job_name and color:
            session['edit_job'] = {
                'id': job_id,
                'name': job_name,
                'color_code': color,
                'color_name': get_color(color)
            }

            return render_template('confirm_edit_job.html')

    return redirect(
            url_for(
                'edit_job.edit_job_page',
                error='入力内容に不備があります。'
            )
        )
