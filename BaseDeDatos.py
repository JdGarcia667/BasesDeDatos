import mariadb

# Establecer la conexión a la base de datos
try:
    conexion = mariadb.connect(
        host="localhost",
        user="tu_usuario",  # reemplaza con tu usuario de MariaDB
        password="tu_contraseña",  # reemplaza con tu contraseña de MariaDB
        database="nombre_de_la_base_de_datos"  # reemplaza con el nombre de tu base de datos
    )
except mariadb.Error as e:
    print(f"Error conectando a la base de datos: {e}")
    exit(1)

# Crear un cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Ejecutar una consulta SQL
cursor.execute("SELECT * FROM tabla")

# Obtener los resultados de la consulta
resultados = cursor.fetchall()

# Mostrar los resultados
for fila in resultados:
    print(fila)

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
