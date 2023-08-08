import sqlite3

def registrar_usuario(nombre_usuario, contraseña):
    conn = sqlite3.connect('bd/usuarios.db')
    cursor = conn.cursor()

    # Insertar el nuevo usuario en la tabla
    cursor.execute("INSERT INTO usuarios (nombre_usuario, contraseña) VALUES (?, ?)", (nombre_usuario, contraseña))

    # Hacer commit para guardar los cambios
    conn.commit()

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    return conn

def Registro():
    print("\n\n\nPagina de Registro\n\n\n")
    print("Ingresa un nombre de usuario:")
    nombre_usuario = input()
    print("Ingresa una contraseña:")
    contraseña = input()

    registrar_usuario(nombre_usuario,contraseña)
    print("Datos insertados correctamente en la base de datos.")
    
