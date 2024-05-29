import mysql.connector

# Establecer la conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="nombre_de_la_base_de_datos"
)

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
