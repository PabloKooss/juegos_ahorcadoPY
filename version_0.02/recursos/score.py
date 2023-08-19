from io import open
nombre_Usuario = "Pablo"
#lista_Palabras = ["Hola","como","te va?"]
score = []
cadena = "\n".join(score)

def score_Escribir():
    score_txt = open(f"bd/{nombre_Usuario}_score.txt","w")
    score_txt.write(cadena)
    score_txt.close()
    
def score_Leer():
    score_txt = open(f"bd/{nombre_Usuario}_score.txt","r")
    lista_recuperada = [linea.strip() for linea in score_txt]
    score.extend(lista_recuperada)
    
def score_Sobreescribir():
    score_txt = open(f"bd/{nombre_Usuario}_score.txt","a")
    score_txt.write(f"\n{cadena}")
    score_txt.close()
    
if __name__ == "__main__":
    #score_Escribir()
    score_Leer()
    #score_Sobreescribir()