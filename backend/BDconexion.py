import mysql.connector

class conexion:
    def __init__(self):
        pass

    def inicia_conexion(self):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12345',
            database='gestion_de_clientes'
        )
        cursor = conn.cursor()
        return cursor, conn 