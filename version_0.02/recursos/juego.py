
def mostrar_tablero(palabra, letras_adivinadas):
    tablero = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero

def juego(nombre_usuario,palabra_Azar):
    letras_adivinadas = []
    intentos = 6

    print("¡Bienvenido al juego de ahorcado",nombre_usuario,"!")
    print(mostrar_tablero(palabra_Azar, letras_adivinadas))

    while True:
        letra = input("Ingresa una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(letra)

        if letra not in palabra_Azar:
            intentos -= 1
            print(f"La letra '{letra}' no está en la palabra. Te quedan {intentos} intentos.")
            if intentos == 0:
                print("¡Has perdido! La palabra secreta era:", palabra_Azar)
                return False
                break

        tablero = mostrar_tablero(palabra_Azar, letras_adivinadas)
        print(tablero)

        if "_" not in tablero:
            print("*"*40,"\n ¡Felicidades! ¡Has adivinado la palabra!\n","*"*40)
            return tablero
            break