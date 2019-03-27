from flask import render_template

from . import bp as main

@main.route('/')
def index():
    return render_template('main/index.html')
