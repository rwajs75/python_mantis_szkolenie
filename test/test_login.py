__autor__ = 'Roman'
from time import sleep
from model.project import Project
from fixture.orm import ORMFixture

# db = ORMFixture(host="localhost", name="bugtracker", user="root", password="")

def test_login(app):
    app.session.login("administrator", "root")
    test = app.soap.project_list("administrator", "root", "Nowy_projekt_")
    print(test)
    # sleep(3)
       # try:
    #     l = db.get_projects_list()
    #     for item in l:
    #         print(item)
    #     print(len(l))
    # finally:
    #     pass
    # old_projects = db.get_projects_list()
    # new_projects = db.get_projects_list()
    # assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
    # print(db.get_projects_list())
    assert app.session.is_logged_in_as("administrator")
