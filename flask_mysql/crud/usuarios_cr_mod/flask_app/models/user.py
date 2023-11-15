from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__( self, data ):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.correo = data["correo"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;" 
        results = connectToMySQL('db_usuarios').query_db(query)
        usuarios = []
        for usuario in results:
            usuarios.append( cls(usuario) )
        return usuarios
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, apellido, correo, created_at, updated_at) VALUES ( %(nombre)s , %(apellido)s, %(correo)s, NOW() , NOW() );" 
        usuario_id = connectToMySQL('db_usuarios').query_db(query, data)
        return usuario_id