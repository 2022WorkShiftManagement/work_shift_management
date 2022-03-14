from flask import Blueprint, render_template, request, session, redirect, url_for

add_work_shift_info = Blueprint('add_work_shift_info', __name__)


@add_work_shift_info.route("/add_work_shift_info")
def add_work_shift_info_page():
    error = request.args.get('error')
    return render_template('add_work_shift_info.html')
