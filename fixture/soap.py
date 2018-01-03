__autor__ = 'Roman'
from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app


    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def project_list(self, project):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            return client.service.mc_project_get_id_from_name("administrator", "root", project)
        except WebFault:
            return False