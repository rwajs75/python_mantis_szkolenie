__autor__ = 'Roman'
# from model.project import Project
from time import sleep

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.app.open_manage_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_xpath("//input[@name='name']").click
        wd.find_element_by_xpath("//input[@name='name']").send_keys(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()


    def delete_by_id(self, id):
        wd = self.app.wd
        self.app.open_project_page(id)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()


    def find_project(self):
        wd = self.app.wd
        self.app.open_manage_page()
        wd.find_elements_


    def get_project_list(self):
        wd = self.app.wd
        self.app.open_manage_page()
