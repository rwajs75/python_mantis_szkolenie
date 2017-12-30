__autor__ = 'Roman'
from time import sleep
import random
import string
from model.project import Project


def test_del_project(app, db):
    if len(db.get_projects_list()) == 0:
        app.project.create(Project(name="Dodany_przed_kasowaniem"))
    old_projects = db.get_projects_list()
    project = random.choice(old_projects)
    app.project.delete_by_id(project.id)
    new_projects = db.get_projects_list()
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


