from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)


    def open_manage_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")) > 0:
            wd.get(self.base_url + "manage_proj_page.php")


    def open_project_page(self, id):
        wd = self.wd
        wd.get(self.base_url + "manage_proj_edit_page.php?project_id=" + id)


    def destroy(self):
        self.wd.quit()
