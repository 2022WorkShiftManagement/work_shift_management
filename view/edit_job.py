from flask import Blueprint, render_template, request, session, redirect, url_for
# from work_shift_management.db import edit_job_db

edit_job = Blueprint('edit_job', __name__)


# バイト先情報登録画面
@edit_job.route("/edit_job")
def edit_job_page():
    if "user" not in session:
        return redirect("/")
    else:
        error = request.args.get('error')
        return render_template(
            'edit_job.html',
            error=error
        )
