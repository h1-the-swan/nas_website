import os
from flask import render_template, url_for, request, json, current_app, redirect, jsonify

from . import bp as main

def get_projects(app, projects_fname='main/projects.json'):
    with app.open_resource('main/projects.json') as f:
        projects = json.load(f)
    return projects

def get_this_project(projects, this_project_url):
    for project in projects:
        if project['url'] == this_project_url:
            return project
    return {}

@main.route('/')
def index():
    projects = get_projects(current_app)
    return render_template('main/index.html', projects=projects, this_project={'name': 'Home'})

@main.route('/vis/')
def redirect_to_home():
    return redirect(url_for('main.index'))

@main.route('/vis/<vis_type>/')
def vis(vis_type='coauthorship'):
    projects = get_projects(current_app)
    this_project = get_this_project(projects, '/vis/' + vis_type)
    template = 'main/' + vis_type + '.html'
    if vis_type == 'coauthorship':
        fname = url_for('static', filename="data/coauthorship/test_coauthorship_graph_combined_max600.json")
    elif vis_type == 'coauthorship1':
        return redirect(url_for('main.coauthorship_scicomm'))
    elif vis_type == 'nautilus':
        fname = url_for('static', filename="data/nautilus/nas2_mag_doi_join_network_fulldata_with_fos_names.json")
    elif vis_type == 'cluster_compare':
        fname = url_for('static', filename="data/cluster_compare/cluster_compare_science_communication_and_misinformation.json")
    elif vis_type == 'keyword_mapping':
        fname = ""
    else:
        # TODO
        fname = ""
        return redirect(url_for('main.index'))
    return render_template(template, projects=projects, vis_type=vis_type, data_fname=fname, this_project=this_project)

@main.route('/vis/coauthorship1/')
def scicomm_redirect():
    return redirect(url_for('main.coauthorship_scicomm'))

@main.route('/methods/')
def methods():
    projects = get_projects(current_app)
    this_project = get_this_project(projects, '/methods')
    return render_template('main/methods.html', projects=projects, this_project=this_project)

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
    projects = get_projects(current_app)
    return render_template('main/nautilus_about.html', projects=projects, this_project={'name': 'Nautilus - About'})

def _extended_bib(data_set=0):
    projects = get_projects(current_app)
    this_project = get_this_project(projects, '/extended_bib')

    fname_0 = url_for('static', filename='data/predictions_sciencecomm_and_misinfo_20190308.tsv')
    fname_1 = url_for('static', filename='data/predictions_combined_sciencecomm_20190719.tsv')
    if data_set == 0:
        fname = fname_0
    elif data_set == 1:
        fname = fname_1
    download_fnames = [
            {'desc': 'Science Comm + Misinformation Papers – Excel format (xlsx)', 'fname': url_for('static', filename='data/predictions_sciencecomm_and_misinfo_20190308.xlsx')},
            {'desc': 'Science Comm + Misinformation Papers – Tab separated format (TSV)', 'fname': fname_0},
            {'desc': 'Science Communication Papers (TSV)', 'fname': fname_1},
    ]
    return render_template('main/extended_bib.html', projects=projects, this_project=this_project, data_fname=fname, download_fnames=download_fnames, ds=data_set)

@main.route('/extended_bib/')
def extended_bib():
    return _extended_bib(0)

@main.route('/extended_bib1/')
def extended_bib1():
    return _extended_bib(1)

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
    projects = get_projects(current_app)
    this_project = get_this_project(projects, '/vis/coauthorship')
    return render_template('main/coauthorship_scicomm.html', projects=projects, this_project=this_project, data_fname=fname)
