from dojos_and_ninjas_app.config.MySQLConnection import connectToMySQL

class Ninja:
    def __init__(self, id, first_name, last_name, age, dojo_id, created_at, updated_at):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.dojo_id = dojo_id
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def add_new_ninja(cls, new_ninja):
        query = "INSERT INTO ninjas(first_name,last_name,age, dojo_id,created_at,updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, SYSDATE(), SYSDATE());"
        data={
            "first_name": new_ninja.first_name,
            "last_name": new_ninja.last_name,
            "age": new_ninja.age,
            "dojo_id": new_ninja.dojo_id
        }

        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
        return result

    @classmethod
    def get_all_ninjas(cls, id):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s"
        data={
            "dojo_id": id
        }
        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
        return result
