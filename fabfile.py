from fabric.api import local
from jinja2 import Environment, FileSystemLoader


template_env = Environment(loader=FileSystemLoader('.'))

def fundamentals():
    build('fundamentals')

def build(pres_name):
    template = template_env.get_template('sources/{}/index.html'.format(pres_name))
    rendered_template = template.render()
    with open('presentations/{}/index.html'.format(pres_name), 'wb') as fh:
        fh.write(rendered_template)

def publish():
    build()
    local('ghp-import -p presentations')
