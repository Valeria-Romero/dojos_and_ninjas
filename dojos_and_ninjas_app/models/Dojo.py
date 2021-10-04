from datetime import date, datetime
from dojos_and_ninjas_app.config.MySQLConnection import connectToMySQL

class Dojo:
    def __init__(self, id, name, created_at, updated_at):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
    

    @classmethod
    def add_dojo(cls, newDojo):
        query = "INSERT INTO dojos(name, created_at, updated_at) VALUES (%(name)s,SYSDATE(),SYSDATE());"
        data = {
            "name": newDojo.name
                }
        result = connectToMySQL( "dojos_and_ninjas_schema" ).query_db( query, data )
        return result

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)

        dojos = []
        for dojo in results:
            dojos.append(Dojo(dojo['id'],dojo['name'],dojo['created_at'],dojo['updated_at']))

        return dojos

    @classmethod
    def get_dojo(cls, id):
        print(id)
        query="SELECT name FROM dojos WHERE id = %(id)s;"
        data={
            "id": id
        }
        result=connectToMySQL( "dojos_and_ninjas_schema" ).query_db( query, data )
        for element in result:
            return element['name']


