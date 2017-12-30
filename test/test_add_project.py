__autor__ = 'Roman'
from time import sleep
import random
import string
from model.project import Project


def test_add_project(app, db):
    old_projects = db.get_projects_list()
    symbols = string.ascii_letters
    project = "Nowy_projekt_" + "".join([random.choice(symbols) for i in range(random.randrange(10))])
    app.project.create(project)
    new_projects = db.get_projects_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
