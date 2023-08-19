import random
from recursos.palabras import *
from recursos.juego import juego
from recursos.score import *
import os
import time

tablero_Facil = []
tablero_Medio = []
tablero_Dificil = []


def juego_Menu(username):
    while True:
        os.system("clear")
        """tablero_Facil = score_Leer(username,carpeta=facil)
        tablero_Medio = score_Leer(username,carpeta=medio)
        tablero_Dificil = score_Leer(username,carpeta=dificil)"""
        resp = input("*"*53+"\n* Bienvenido al juego del ahorcado este es el menu: *\n"+"*"*53+"\n1.-  Nivel Facil\n2.-  Nivel Medio\n3.-  Nivel Dificil\n4.-  Tablero\n5.-  Menu principal\n")
        match resp:
            case "1":
                palabra_Azar = random.choice(facil)
                tablero=juego(username,palabra_Azar)
                if tablero != False:
                    tablero_Facil.append(tablero[::2]) 
                    print(tablero[::2])
                    time.sleep(4)
            case "2":
                palabra_Azar = random.choice(medio)
                tablero=juego(username,palabra_Azar)
                if tablero != False:
                    tablero_Medio.append(tablero[::2]) 
                    print(tablero[::2])
                    time.sleep(4)
            case "3":
                palabra_Azar = random.choice(dificil)
                tablero=juego(username,palabra_Azar)
                if tablero != False:
                    tablero_Dificil.append(tablero[::2]) 
                    print(tablero[::2])
                    time.sleep(4)
            case "4":
                os.system("clear")
                print(f"{username} estas son las palabras que has adivinado:")
                print("Facil:")
                print(tablero_Facil)
                print("Medio:")
                print(tablero_Medio)
                print("Dicifil:")
                print(tablero_Dificil)
                time.sleep(4)
            case "5":
                print("Elegiste salir")
                
                break
            case _:
                pass