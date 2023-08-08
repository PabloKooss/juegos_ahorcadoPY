import sqlite3

conexion = sqlite3.connect('bd/usuarios.db')
cursor = conexion.cursor()

consulta = "SELECT * FROM usuarios"
cursor.execute(consulta)

registros = cursor.fetchall()
for registro in registros:
    print(registro)

conexion.close()
