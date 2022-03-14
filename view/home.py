from types import resolve_bases
from flask import Flask, Blueprint, render_template, request, redirect, jsonify


home = Blueprint('home',__name__, url_prefix='/home')

@home.route('/')
def home_index():
   return render_template('home.html')


