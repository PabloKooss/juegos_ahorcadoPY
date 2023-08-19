import pwinput
from juego.menu import juego_Menu
import os

class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
usuarios_db = [
    Usuario("Pablo", "1234"),
    Usuario("invitado", "invitado"),
    Usuario("usuario", "contraseña")
]

def verificar_credenciales(username, password):
    for usuario in usuarios_db:
        if usuario.username == username and usuario.password == password:
            return True
    return False

def acceso():
    while True:
        os.system("clear")
        resp = input("¿Quieres iniciar sesion?\nSi\nNo\n")
        if resp == "Si" or resp == "si" or resp ==  "SI":
            os.system("clear")
            print("Inicio de sesión.")
            username = input("Ingresa tu nombre de usuario: ")
            password = pwinput.pwinput("Ingresa tu contraseña: ")

            match verificar_credenciales(username, password):
                case True:
                    juego_Menu(username)
                    
                case False:
                    print("Credenciales incorrectas. Intenta de nuevo.")
                case "S":
                    break
        else:
            break
