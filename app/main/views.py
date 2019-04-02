import os
from flask import render_template, url_for, request, json, current_app, redirect

from . import bp as main

def get_projects(app, projects_fname='main/projects.json'):
    with app.open_resource('main/projects.json') as f:
        projects = json.load(f)
    return projects

@main.route('/')
def index():
    projects = get_projects(current_app)
    return render_template('main/index.html', projects=projects)

@main.route('/vis/<vis_type>/')
def vis(vis_type):
    projects = get_projects(current_app)
    template = 'main/' + vis_type + '.html'
    if vis_type == 'coauthorship':
        fname = url_for('static', filename="data/coauthorship/test_coauthorship_graph_combined_max600.json")
    elif vis_type == 'nautilus':
        fname = url_for('static', filename="data/nautilus/nas2_mag_doi_join_network_fulldata_with_fos_names.json")
    elif vis_type == 'cluster_compare':
        fname = url_for('static', filename="data/cluster_compare/cluster_compare_science_communication_and_misinformation.json")
    else:
        # TODO
        fname = ""
        return redirect(url_for('main.index'))
    return render_template(template, projects=projects, vis_type=vis_type, data_fname=fname)

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
