from fabric.api import local
from jinja2 import Environment, FileSystemLoader


template_env = Environment(loader=FileSystemLoader('.'))

presentations = [{'name': 'fundamentals', 'title': 'Hadoop Fundamentals'}]
                 #{'name': 'operational', 'title': 'Hadoop Operational'}]

def build_all():
    [build(pres['name']) for pres in presentations]
    build_index()

def build_index():
    '''build the index file for all the presentations'''
    template = template_env.get_template('sources/index.html')
    rendered_template = template.render(presentations=presentations)
    with open('presentations/index.html', 'wb') as fh:
        fh.write(rendered_template)

def operational():
    build('operational')

def fundamentals():
    build('fundamentals')

def build(pres_name):
    template = template_env.get_template('sources/{}/index.html'.format(pres_name))
    rendered_template = template.render()
    with open('presentations/{}/index.html'.format(pres_name), 'wb') as fh:
        fh.write(rendered_template)

def publish():
    build_all()
    local('ghp-import -p presentations')
