__autor__ = 'Roman'
from time import sleep
import random
import string
from model.project import Project


def test_add_project(app):
    # old_projects = db.get_projects_list()
    symbols = string.ascii_letters
    project = "Nowy_projekt_" + "".join([random.choice(symbols) for i in range(random.randrange(15))])
    app.project.create(project)
    print(project)
    assert app.soap.project_list(project) > 0
    # new_projects = db.get_projects_list()
    # old_projects.append(project)
    # assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
