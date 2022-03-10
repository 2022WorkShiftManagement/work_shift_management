from flask import Flask, Blueprint, render_template, redirect, request, url_for, session

create_group = Blueprint('create_group', __name__, url_prefix='/create-group')
