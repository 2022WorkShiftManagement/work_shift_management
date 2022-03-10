from flask import Flask, Blueprint, render_template, redirect, request, url_for, session

create_group = Blueprint('create_group', __name__, url_prefix='/create-group')


@create_group.route("/", methods=['GET'])
def create_group_form():
    # if "user_id" not in session:  # セッションの有無
    #     return redirect("/")
    return render_template("create_group.html")