from flask import Blueprint, render_template, request, session, redirect, url_for
from db import job_db

from function.color import get_color


job = Blueprint('job', __name__, url_prefix='/job')


# バイト先情報登録画面
@job.route("/add_job")
def add_job_page():
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
@job.route("/confirm_add_job", methods=["POST"])
def confirm_add_job_page():
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
@job.route("/insert_job")
def insert_job():
    if "user" not in session:
        return redirect("/")
    else:
        insert_result = job_db.insert_work_shift_info(
            session['user'],
            session['job']['name'],
            session['job']['color_code']
        )

        # データベースに登録できたか
        if insert_result:
            return redirect("/home")

        return redirect(
            url_for(
                'job.add_job_page',
                error='登録に失敗しました。'
            )
        )


# バイト先情報編集画面
@job.route("/edit_job")
def edit_job_page():
    if "user" not in session:
        return redirect("/")
    else:
        error = request.args.get('error')

        # ユーザの登録しているバイト先を取得
        job_list = job_db.get_user_job(session['user'])

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
@job.route("/confirm_edit_job", methods=["POST"])
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
            'job.edit_job_page',
            error='入力内容に不備があります。'
        )
    )


# バイト先情報登録
@job.route("/update_job")
def update_job():
    if "user" not in session:
        return redirect("/")
    else:
        update_result = job_db.update_job(
            session['user'],
            session['edit_job']['id'],
            session['edit_job']['name'],
            session['edit_job']['color_code']
        )

        # データベースに登録できたか
        if update_result:
            return redirect("/home")

        return redirect(
            url_for(
                'job.edit_job_page',
                error='登録に失敗しました。'
            )
        )
