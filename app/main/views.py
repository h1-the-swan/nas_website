import os
from flask import render_template, url_for, request, json, current_app, redirect, jsonify

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
        this_project = projects[0]
    elif vis_type == 'nautilus':
        fname = url_for('static', filename="data/nautilus/nas2_mag_doi_join_network_fulldata_with_fos_names.json")
        this_project = projects[1]
    elif vis_type == 'cluster_compare':
        fname = url_for('static', filename="data/cluster_compare/cluster_compare_science_communication_and_misinformation.json")
        this_project = projects[2]
    elif vis_type == 'keyword_mapping':
        fname = ""
        this_project = projects[4]
    else:
        # TODO
        fname = ""
        return redirect(url_for('main.index'))
    return render_template(template, projects=projects, vis_type=vis_type, data_fname=fname, this_project=this_project)

@main.route('/coauthorship/')
def coauthorship_vis():
    # fname = url_for('static', filename="data/coauthorship/test_coauthorship_graph_combined_max600.json")
    # return render_template('main/coauthorship.html', data_fname=fname)
    return redirect(url_for('main.vis', vis_type='coauthorship'))

@main.route('/nautilus/')
def nautilus_vis():
    return redirect(url_for('main.vis', vis_type='nautilus'))

@main.route('/clustervis/')
def cluster_compare_vis():
    return redirect(url_for('main.vis', vis_type='cluster_compare'))

@main.route('/vis/nautilus/about/')
def nautilus_about():
    return render_template('main/nautilus_about.html')

@main.route('/extended_bib/')
def extended_bib():
    projects = get_projects(current_app)
    this_project = projects[3]
    fname = url_for('static', filename='data/predictions_sciencecomm_and_misinfo_20190308.tsv')
    download_fnames = [
            {'desc': 'Excel format (xlsx)', 'fname': url_for('static', filename='data/predictions_sciencecomm_and_misinfo_20190308.xlsx')},
            {'desc': 'Tab separated format (TSV)', 'fname': fname},
    ]
    return render_template('main/extended_bib.html', projects=projects, this_project=this_project, data_fname=fname, download_fnames=download_fnames)

@main.route('/keywords/')
def keyword_mapping():
    return redirect(url_for('main.vis', vis_type='keyword_mapping'))

@main.route('/demo/')
def nautilus_demo():
    projects = get_projects(current_app)
    this_project = projects[1]
    fname = url_for('static', filename="data/nautilus/nas2_mag_doi_join_network_fulldata_with_fos_names.json")
    return render_template('main/nautilus_demo.html', projects=projects, vis_type='nautilus', data_fname=fname, this_project=this_project)

@main.route('/comm/')
def coauthorship_scicomm():
    fname = url_for('static', filename="data/coauthorship/science_communication_papers_plus_extended_relevant_coauthor.json")
    return render_template('main/coauthorship_scicomm.html', data_fname=fname)
