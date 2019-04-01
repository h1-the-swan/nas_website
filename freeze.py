from flask import json
from flask_frozen import Freezer
from app import create_app

freezer = Freezer()
app = create_app(config='production')

def get_projects(app, projects_fname='main/projects.json'):
    with app.open_resource('main/projects.json') as f:
        projects = json.load(f)
    return projects

freezer.init_app(app)

projects = get_projects(app)

@freezer.register_generator
def vis():
    for project in projects:
        vis_type = project['url'].split('/')[-1]
        # yield (endpoint, values) tuple
        yield ('main.vis', {'vis_type': vis_type})

if __name__ == '__main__':
    freezer.freeze()
