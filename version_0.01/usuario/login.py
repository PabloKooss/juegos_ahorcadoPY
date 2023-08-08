import sqlite3
import pwinput
from niveles.menu import menu

def verificar_login(nombre_usuario, contraseña):
    conn = sqlite3.connect('bd/usuarios.db')
    cursor = conn.cursor()

    # Consulta para obtener el usuario con el nombre de usuario proporcionado
    cursor.execute("SELECT * FROM usuarios WHERE nombre_usuario = ?", (nombre_usuario,))

    # Obtener el registro del usuario
    usuario = cursor.fetchone()

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    # Verificar si se encontró el usuario y si la contraseña coincide
    if usuario is not None and usuario[2] == contraseña:
        datos_usuario=nombre_usuario
        return True
    else:
        return False


def verificar():
    # Verificar el inicio de sesión de un usuario
    print("--------------------\nLogin\n--------------------\nIngresa tu usuario:")
    nombre_usuario = input()
    contraseña=pwinput.pwinput()
    if verificar_login(nombre_usuario, contraseña):
        menu(nombre_usuario)
    else:
        print("Credenciales incorrectas.")
