#Importando Libreria mysql.conector para conectar python con MySQL
import mysql.connector

def connectionBD():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="app_empresa_bd",
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci',
            raise_on_warnings=True
        )
        if connection.is_connected():
            return connection
        
    except mysql.connector. Error as error:
        print(f"No se pudo conectar: {error}")