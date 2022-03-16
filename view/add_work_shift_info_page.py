from flask import Blueprint, render_template, request, session, redirect, url_for

add_work_shift_info = Blueprint('add_work_shift_info', __name__)


@add_work_shift_info.route("/add_work_shift_info")
def add_work_shift_info_page():
    error = request.args.get('error')
    return render_template(
        'add_work_shift_info.html',
        color=get_color(),
        error=error
    )


@add_work_shift_info.route("/confirm_work_shift_info", methods=["POST"])
def confirm_work_shift_info_page():
    job_name = request.form.get('job_name')
    job_color = request.form.get('color')

    if job_name and job_color:
        session['job'] = {
            'name': job_name,
            'color_code': job_color,
            'color_name': get_color(job_color)
        }

        return render_template('confirm_work_shift_info.html')

    return redirect(
        url_for(
            'add_work_shift_info.add_work_shift_info_page',
            error='入力内容に不備があります。'
        )
    )


def get_color(key=None):
    color = {
        "#FF0000": "レッド",
        "#FF3399": "ピンク",
        "#FF9100": "オレンジ",
        "#FFD400": "イエロー",
        "#008000": "グリーン",
        "#B2D235": "イエローグリーン",
        "#67A7CC": "スカイブルー",
        "#0067C0": "ブルー",
        "#5F4894": "パープル",
        "#717375": "グレー"
    }

    if key:
        return color[key]

    return color
