import os
from flask import render_template, url_for, request, json, current_app, redirect

from . import bp as main

@main.route('/')
def index():
    with current_app.open_resource('main/projects.json') as f:
        projects = json.load(f)
    print(projects)
    return render_template('main/index.html', projects=projects)

@main.route('/coauthorship/')
def coauthorship_vis():
    fname = url_for('static', filename="data/coauthorship/test_coauthorship_graph_combined_max600.json")
    return render_template('main/coauthorship.html', data_fname=fname)

@main.route('/nautilus/')
def nautilus_vis():
    # TODO
    return redirect(url_for('main.index'))

@main.route('/clustervis/')
def cluster_compare_vis():
    # TODO
    return redirect(url_for('main.index'))

@main.route('/extended_bib/')
def extended_bib():
    # TODO
    return redirect(url_for('main.index'))

@main.route('/keywords/')
def keyword_mapping():
    # TODO
    return redirect(url_for('main.index'))
