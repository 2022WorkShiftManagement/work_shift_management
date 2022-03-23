from flask import Blueprint, render_template, request, session, redirect, url_for
from db import edit_account_db

edit_account = Blueprint('edit_account', __name__)


# バイト先情報登録画面
@edit_account.route("/edit_account")
def edit_account_page():
    if "user" not in session:
        return redirect("/")
    else:
        account = edit_account_db.search_account(session['user'])
        error = request.args.get('error')
        return render_template(
            'edit_account.html',
            account=account,
            error=error
        )


