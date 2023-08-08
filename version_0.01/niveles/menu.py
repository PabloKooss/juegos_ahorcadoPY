from niveles.facil.nivel1 import facil
'''from niveles.nivel2 import juego_n2
from niveles.nivel3 import juego_n3
from niveles.nivel4 import juego_n4'''
puntuacion=[]

def menu(nombre_usuario):
    print("Seleciona una opcion")
    while True:
        nivel=int(input(" Opcion          1\n Opcion          2\n Tablero         3\n Menu de inicio  4\n"))
        if nivel==1:
            tablero=facil(nombre_usuario)
        elif nivel==2:
            print("Elegiste nivel 1")
            print(nombre_usuario)
            print("este es el tablero")
        elif nivel==3:
            print("Elegiste Tablero")
            print(f"{nombre_usuario} a adivinado {tablero}")
        elif nivel==4:
            print("Menu de inicio\n\n")
            break
        else:
            print("Respuesta invalida\nINGRESA UNA OPCION VALIDA")
