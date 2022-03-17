from flask import Blueprint, render_template, request, session, redirect, url_for
from db import edit_job_db
from function.color import get_color

edit_job = Blueprint('edit_job', __name__)


# バイト先情報登録画面
@edit_job.route("/edit_job")
def edit_job_page():
    if "user" not in session:
        return redirect("/")
    else:
        error = request.args.get('error')

        job_list = edit_job_db.get_user_job(session['user'])
        for job in job_list:
            job['color_name'] = get_color(job['color'])

        print(job_list)
        return render_template(
            'edit_job.html',
            job_list=job_list,
            color_list=get_color(),
            error=error
        )
