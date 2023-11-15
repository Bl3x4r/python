from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import modelo_ninjas
from flask_app import BASE_DATOS

class Dojo:
    def __init__(self, datos):
        self.id = datos["id"]
        self.nombre = datos["nombre"]
        self.created_at = datos["created_at"]
        self.updated_at = datos["updated_at"]
        self.ninjas = []
    @classmethod
    def agregar_uno(cls, datos):
        query ="INSERT INTO dojos(nombre) VALUES(%(nombre)s)"
        return connectToMySQL(BASE_DATOS).query_db(query, datos)
    
    @classmethod
    def seleccionar_todos(cls):
        query = """
                SELECT *
                FROM dojos;
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query)
        lista_dojos = []
        for renglon in resultado:
            lista_dojos.append(Dojo(renglon))
        return lista_dojos
    @classmethod
    def seleccionar_uno_con_ninjas(cls, datos):
        query = """
                SELECT * FROM dojos LEFT JOIN ninjas
                ON dojos.id = ninjas.dojo_id
                WHERE dojos.id = %(dojo_id)s;
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query, datos)
        dojo = Dojo(resultado[0])
        for renglon in resultado:
            if renglon['edad'] != None:
                ninja={
                    'id' : renglon['ninjas.id'],
                    'nombre' : renglon['ninjas.nombre'],
                    'apellido' : renglon['apellido'],
                    'edad' : renglon['edad'],
                    'created_at' : renglon['ninjas.created_at'],
                    'updated_at': renglon['ninjas.updated_at'],
                    'dojo_id' : renglon['id']
                }
                dojo.ninjas.append(modelo_ninjas.Ninja(ninja))
        return dojo