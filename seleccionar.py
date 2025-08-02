class CRUD:

    from sqlite3 import connect
    import string
    import mysql.connector

    def __init__(self):
        pass

    def __inicia_Conexion(self):
        global conn, Cursor
        conn = self.mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '12345',
            database = 'gestion_de_clientes'
            )
        Cursor = conn.cursor()
    #----------------------------------------------#
    

    #--------#
    def login (self, usuario:string, contrasena:string):
        self.__inicia_Conexion()
        consulta = "SELECT * FROM sesion WHERE correo = %s AND contraseña = %s"
        valores = (usuario, contrasena)

        Cursor.execute(consulta, valores)
        resultado = Cursor.fetchone()
        conn.close()

        if resultado:
            return True
        else:
            return False
    #--#

    def sing_up (self, correo:string, contrasena:string):
        self.__inicia_Conexion()
        consulta = "INSERT INTO sesion (correo, contraseña) VALUES (%s, %s)"
        valores = (correo, contrasena)

        Cursor.execute(consulta, valores)
        conn.commit()
        conn.close()
    #--------#


    def insert (self, nombre:string, identificador:string, telefono:string, etiqueta:int, descripcion:string):
        self.__inicia_Conexion()
        consulta = "INSERT INTO Cliente (nombre, identificador, telefono, etiqueta, descripcion) VALUES (%s, %s, %s, %s, %s)"
        valores = (nombre, identificador, telefono, etiqueta, descripcion)

        Cursor.execute(consulta, valores)
        conn.commit()
        conn.close()

    #--#

    def update (self, nombre:string, identificador:string, telefono:string, etiqueta:int, descripcion:string, id:int):
        self.__inicia_Conexion()
        consulta = "UPDATE Cliente SET nombre = %s, identificador = %s, telefono = %s, etiqueta = %s, descripcion = %s WHERE id = %s"
        valores = (nombre, identificador, telefono, etiqueta, descripcion, identificador, id)

        Cursor.execute(consulta, valores)
        conn.commit()
        conn.close()

    #--#

    def delete (self, id:int):
        self.__inicia_Conexion()
        consulta = "DELETE FROM Cliente WHERE Id = %s"
        valores = (id,)

        Cursor.execute(consulta, valores)
        conn.commit()
        conn.close()
    #----------------------------------------------#




result = CRUD()
user =input("informa el usuario: ")
passw = input("informa la contraseña: ")
print(result.login(user, passw))

