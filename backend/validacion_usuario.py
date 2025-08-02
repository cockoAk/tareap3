from backend.BDconexion import conexion
import mysql.connector

class validacion_usuario:
    def __init__(self):
        self.con = conexion()
        self.cursor, self.conn = self.con.inicia_conexion()

    def login(self, correo, contrasena):
        query = "SELECT * FROM sesion WHERE correo = %s AND contraseña = %s"
        self.cursor.execute(query, (correo, contrasena))
        resultado = self.cursor.fetchone()
        self.conn.close()  
        
        return resultado is not None

    def __del__(self):
        if hasattr(self, 'conn'):
            self.conn.close()