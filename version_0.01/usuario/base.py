import sqlite3
def base():
    # Crear una conexión a la base de datos (o conectar a una existente)
    conn = sqlite3.connect('bd/usuarios.db')
    # Crear un cursor para ejecutar las consultas
    cursor = conn.cursor()
    # Crear tabla de usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_usuario TEXT NOT NULL,
            contraseña TEXT NOT NULL
        )
    ''')
    # Hacer commit para guardar los cambios
    conn.commit()
    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()
