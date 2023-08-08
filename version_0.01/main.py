#librerias necesarias
from usuario.base import base
from usuario.login import verificar
from usuario.registro import Registro
#-----------Creacion y conexion con base de datos---------------------
base()
#----------------------------------Inicio de programa-------------------------

print("**********************\n* Juego de ahorcado  *\n**********************")
while True:
    opcion= input('Elige una opción\nIngresar ---> 1\nRegistrar nuevo usuario ---> 2\nSalir ---> S\n')
    if opcion=="1":
        verificar()
    elif opcion=="2":
        Registro()
    elif opcion=="S" or opcion=="s":
        print("Buen dia")
        break
    else:
        print("Respuesta invalida\nINGRESA UNA OPCION VALIDA")
print("Fin de juego")
