import mysql.connector
from mysql.connector import Error

def connect_to_mariadb():
    try:
        # Conexión a la base de datos
        connection = mysql.connector.connect(
            host='nodo1',  # Dirección del servidor remoto
            port=3306,  # Puerto de MariaDB
            database='nombre_de_tu_base_de_datos',  # Reemplaza con el nombre de tu base de datos
            user='tu_usuario',  # Reemplaza con tu nombre de usuario
            password='tu_contraseña'  # Reemplaza con tu contraseña
        )

        if connection.is_connected():
            print("Conexión exitosa a la base de datos")

            # Crear un cursor para realizar operaciones en la base de datos
            cursor = connection.cursor()

            # Ejecutar una consulta
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("Conectado a la base de datos: ", record)

            # Aquí puedes ejecutar más consultas
            cursor.execute("SHOW TABLES;")
            tables = cursor.fetchall()
            print("Tablas en la base de datos: ")
            for table in tables:
                print(table)

    except Error as e:
        print("Error al conectar a MariaDB", e)

    finally:
        # Cerrar la conexión a la base de datos
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("Conexión a MariaDB cerrada")

if __name__ == "__main__":
    connect_to_mariadb()
