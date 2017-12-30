__autor__ = 'Roman'
from pony.orm import *
from datetime import datetime
from model.project import Project
from pymysql.converters import decoders


class ORMFixture:

    db = Database()

    class ORMProject(db.Entity):
        _table_ = 'mantis_project_table'
        id = PrimaryKey(int, column='id')
        name = Optional(str, column='name')


    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)


    def convert_projects_to_model(self, projects):
        def convert(project):
            return Project(id=str(project.id), name=project.name)
        return list(map(convert, projects))


    @db_session
    def get_projects_list(self):
        return self.convert_projects_to_model(select(p for p in ORMFixture.ORMProject))
