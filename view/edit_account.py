from flask import Blueprint, render_template, request, session, redirect, url_for
from db import edit_account_db
from function import user_function

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


# バイト先情報登録確認画面
@edit_account.route("/update_account", methods=["POST"])
def update_account():
    if "user" not in session:
        return redirect("/")
    else:
        user_name = request.form.get('user_name')
        current_pw = request.form.get('current_pw')
        new_pw = request.form.get('new_pw')
        re_new_pw = request.form.get('re_new_pw')

        # 入力チェック
        if user_name and current_pw and new_pw and re_new_pw:
            # 今のパスワードでアカウントを取得
            current_pw_check = edit_account_db.search_account(session['user'], current_pw)
            # アカウントを取得できなかった時
            if not current_pw_check:
                return redirect(url_for('edit_account.edit_account_page', error='パスワードが間違っています。'))
            # 新しいパスワードと再入力が等しくないとき
            if new_pw != re_new_pw:
                return redirect(url_for('edit_account.edit_account_page', error='パスワードが等しくありません。'))

            # 名前の文字数が３２文字以内か
            if not user_function.max_length_validation(user_name, 32):
                return redirect(url_for('edit_account.edit_account_page', error='名前の文字数は３２文字までです。'))

            # アカウントの編集
            update_result = edit_account_db.update_account(
                session['user'],
                user_name,
                new_pw
            )

            # データベースに登録できたか
            if update_result:
                return redirect("/logout")

            # 入力に不備があったら入力画面へリダイレクト
            return redirect(
                url_for(
                    'edit_account.edit_account_page',
                    error='編集に失敗しました。'
                )
            )

        # 入力に不備があったら入力画面へリダイレクト
        return redirect(
            url_for(
                'edit_account.edit_account_page',
                error='入力内容に不備があります。'
            )
        )
