from flask import render_template, url_for, request, config

from . import bp as main

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/coauthorship/')
def coauthorship_vis():
    fname = url_for('static', filename="data/coauthorship/test_coauthorship_graph_combined_max600.json")
    return render_template('main/coauthorship.html', data_fname=fname)
