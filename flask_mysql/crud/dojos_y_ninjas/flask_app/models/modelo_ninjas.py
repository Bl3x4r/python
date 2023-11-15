from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import BASE_DATOS

class Ninja:
    def __init__(self, datos):
        self.id = datos['id']
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.edad = datos['edad']
        self.created_at = datos['created_at']
        self.updated_at = datos['updated_at']
        self.dojo_id = datos['dojo_id']

    @classmethod
    def agregar_uno(cls, datos):
        query = """
                INSERT INTO ninjas(nombre, apellido, edad, dojo_id)
                VALUES(%(nombre)s,%(apellido)s,%(edad)s,%(dojo_id)s);
                """
        return connectToMySQL(BASE_DATOS).query_db(query, datos)