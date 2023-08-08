import random
# Lista de palabras para el juego
palabras = ['python', 'programacion', 'desarrollo', 'tecnologia', 'inteligencia', 'artificial']

def seleccionar_palabra():
    # Seleccionar una palabra aleatoria de la lista de palabras
    return random.choice(palabras)

def mostrar_tablero(palabra, letras_adivinadas):
    # Mostrar el tablero con las letras adivinadas y espacios en blanco para las letras no adivinadas
    tablero = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero

def facil(nombre_usuario):
    palabra_secreta = seleccionar_palabra()
    letras_adivinadas = []
    intentos = 6

    print("¡Bienvenido al juego de ahorcado",nombre_usuario,"!")
    print(mostrar_tablero(palabra_secreta, letras_adivinadas))

    while True:
        letra = input("Ingresa una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(letra)

        if letra not in palabra_secreta:
            intentos -= 1
            print(f"La letra '{letra}' no está en la palabra. Te quedan {intentos} intentos.")
            if intentos == 0:
                print("¡Has perdido! La palabra secreta era:", palabra_secreta)
                break

        tablero = mostrar_tablero(palabra_secreta, letras_adivinadas)
        print(tablero)

        if "_" not in tablero:
            print("¡Felicidades! ¡Has adivinado la palabra!")
            return tablero
            break
if __name__ == "__main__":
    facil()
